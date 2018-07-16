import json
import os
from django.http import JsonResponse, HttpResponse
from django.contrib.auth.decorators import login_required
from django.template import Context, Template
from django.contrib.auth import authenticate, login
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import redirect
from django.shortcuts import render
from django.contrib.auth.models import User

from App.Utilities import S3Access, dynamoAccess
from pyReturn.response import status_response as sr

# Templating
from django.template import loader

# QueryDict
from django.http import QueryDict

# uuid
import uuid

# load model
from .models import City, Story

# time zone
from django.utils import timezone

# import endpoints
from endpoints import endpoints, BUCKET_NAME

# constants
DYNAMO_STORY_TABLE = 'STORY_TABLE'
DEFAULT_COVER_IMAGE = 'https://towntory-public-host.s3.amazonaws.com/default.png'


"""
|_______________________________________
|   Heathcheck|
|_______________________________________
"""
def healthcheck(request):
    text = 'Up and running'
    return HttpResponse(text)

"""
|_______________________________________
|   Langing Page|
|_______________________________________
"""
#landing Page Upload to post address
def landing(request):
    status = sr()
    if request.method == 'GET':
        template = loader.get_template('landing.html')
        context = {
            'endpoints': endpoints,
            'login': request.user.is_authenticated,
        }
        return HttpResponse(template.render(context, request))
    return JsonResponse(status.data)

"""
|_______________________________________
|   Read City|
|_______________________________________
"""
def city(request):
    status = sr()
    if request.method == 'GET':
        city_name = request.GET.get('city_name')
        try:
            # city has story
            city = City.objects.get(pk=city_name)
            stories = Story.objects.filter(city=city).order_by('-datetime')
        except:
            # city has no story
            stories = None
        # render stories
        template = loader.get_template('city.html')
        context = {
            'city_name': city_name,
            'stories': stories,
            'endpoints': endpoints,
        }
        return HttpResponse(template.render(context, request))
    return JsonResponse(status.data)



"""
|_______________________________________
|   Read Story|
|_______________________________________
"""
def story(request):
    status = sr()
    if request.method == 'GET':
        story_id = request.GET.get('story_id')
        story = Story.objects.get(id=story_id)
        title = story.title
        summary = story.summary
        cover_url = story.cover
        author = story.author
        city_name = story.city.city
        template = loader.get_template('story.html')
        content = dynamoAccess.get_item(DYNAMO_STORY_TABLE, 'story_id', story_id)['content']
        is_author = (request.user.username == str(author)) or request.user.is_staff
        context = {
            'title': title,
            'summary': summary,
            'content': content,
            'endpoints': endpoints,
            'cover_url': cover_url,
            'city_name': city_name,
            'author': author,
            'is_author': is_author,
            'story_id': story_id,
        }
        return HttpResponse(template.render(context, request))
    return JsonResponse(status.data)

"""
|_______________________________________
|   Write Story|
|_______________________________________
"""
def uploadImg(request):
    status = sr()
    file = None
    if request.method == 'POST':
        image = request.FILES['image']
        url = S3Access.upload_file(BUCKET_NAME, image.file)
    status.attach_data('url', url, True)
    return JsonResponse(status.data)

def uploadImgURL(request):
    status = sr()
    if request.user.is_authenticated:
        if request.method == 'GET':
            uploadURL, accessURL = S3Access.generate_presigned_upload_url(BUCKET_NAME)
        status.attach_data('uploadURL', uploadURL, True)
        status.attach_data('accessURL', accessURL, True)
    else:
        status.set_errorMessage('not logged in')
    return JsonResponse(status.data)

def uploadImgURLs(request):
    status = sr()
    if request.user.is_authenticated:
        if request.method == 'GET':
            imageCount = request.GET.get('imageCount')
            uploadURLs = []
            accessURLs = []
            for i in range(int(imageCount)):
                uploadURL, accessURL = S3Access.generate_presigned_upload_url(BUCKET_NAME)
                uploadURLs.append(uploadURL)
                accessURLs.append(accessURL)
        status.attach_data('uploadURLs', uploadURLs, True)
        status.attach_data('accessURLs', accessURLs, True)
    else:
        status.set_errorMessage('not logged in')
    return JsonResponse(status.data)

def uploadArticle(request):
    status = sr()
    if request.user.is_authenticated:
        if request.method == 'POST':
            title = request.POST.get('title')
            summary = request.POST.get('summary')
            article = request.POST.get('article')
            print(article)
            city = request.POST.get('city')
            # if city not exsit, create one
            try:
                city = City.objects.get(pk=city)
            except:
                city_name, state_name, country_name = city.split(', ')
                lat = float(request.POST.get('latitude'))
                lng = float(request.POST.get('longitude'))
                city = City.objects.create(city=city, city_name=city_name, 
                    latitude=lat, longitude =lng, state_name=state_name, country_name=country_name)
            # get current user
            user = request.user
            # create story
            ID = str(uuid.uuid4())
            # use dynamoDB to store the contents
            article = json.loads(article)
            # check if there is any image and get the first one as cover
            cover_img_url = DEFAULT_COVER_IMAGE
            for item in article:
                if item[0] == 'image':
                    cover_img_url = item[1]
                    break
            # add one story and save the update
            city.number_of_story += 1
            city.save()
            # now save the article content
            dynamoAccess.add(DYNAMO_STORY_TABLE, 'story_id', ID, content = article)
            # save the story
            story = Story.objects.create(id = ID, city = city, author = user, title = title, summary = summary, cover = cover_img_url, datetime = timezone.now())
            status.attach_data('story_id', ID, isSuccess=True)
        status.set_errorMessage('not post')
    else:
        status.set_errorMessage('not logged in')
    return JsonResponse(status.data)

def write(request):
    if request.user.is_authenticated:
        status = sr()
        if request.method == 'GET':
            city_name = request.GET.get('city_name')
            template = loader.get_template('write.html')
            context = {
                'endpoints': endpoints,
                'city_name': city_name,
            }
            return HttpResponse(template.render(context, request))
    else:
        return redirect(endpoints['login_url'] + '?next=/app/write')

"""
|_______________________________________
|   Delete Story|
|_______________________________________
"""
@csrf_exempt
def deleteStory(request):
    status = sr()
    if request.method == 'DELETE':
        story_id = request.GET.get('story_id')
        try:
            # check if the object exist
            story = Story.objects.get(pk=story_id)
            # check if the current user if the author
            if (request.user == story.author) or request.user.is_staff:
                # retrieve data list from DynamoDB
                content = dynamoAccess.get_item(DYNAMO_STORY_TABLE, 'story_id', story_id)['content']
                # based on the list delete objects in S3
                for item in content:
                    if item[0] == 'image':
                        key = item[1].split('/')[-1]
                        S3Access.delete_object(BUCKET_NAME, key)
                # delete dynamoDB record
                dynamoAccess.delete(DYNAMO_STORY_TABLE, 'story_id', story_id)
                # reduce story count of a city
                city = story.city
                city.number_of_story -= 1
                city.save()
                # delete story object from SQL DB
                story.delete()
                # set status to success
                status.set_status(True)
            else:
                status.set_errorMessage('not authorized')

        except Story.DoesNotExist:
            status.set_errorMessage('story not exist')

    return JsonResponse(status.data)

"""
|_______________________________________
|   Discover|
|_______________________________________
"""
# experimental map function
def discover(request):
    status = sr()
    if request.method == 'GET':
        city_list = []
        cities = City.objects.all()
        for city in cities:
            city_list.append([city.city, city.number_of_story, city.latitude, city.longitude])

        template = loader.get_template('discover.html')
        context = {
            'endpoints': endpoints,
            'city_list': city_list,
        }
        return HttpResponse(template.render(context, request))
    return JsonResponse(status.data)

"""
|_______________________________________
|   Extra information|
|_______________________________________
"""
#about page link
def about(request):
    status = sr()
    if request.method == 'GET':
        template = loader.get_template('about.html')
        context = {
            'endpoints': endpoints,
        }
        return HttpResponse(template.render(context, request))
    return JsonResponse(status.data)

#contact page link
def contact(request):
    status = sr()
    if request.method == 'GET':
        template = loader.get_template('contact.html')
        context = {
            'endpoints': endpoints,
        }
        return HttpResponse(template.render(context, request))
    return JsonResponse(status.data)

# privacy policy
def privacy_policy(request):
    status = sr()
    if request.method == 'GET':
        template = loader.get_template('privacypolicy.html')
        context = {
            'endpoints': endpoints,
        }
        return HttpResponse(template.render(context, request))
    return JsonResponse(status.data)

# term of services
def term_of_services(request):
    status = sr()
    if request.method == 'GET':
        template = loader.get_template('termofservices.html')
        context = {
            'endpoints': endpoints,
        }
        return HttpResponse(template.render(context, request))
    return JsonResponse(status.data)

#profile link
def profile(request):
    status = sr()
    if request.method == 'GET':
        template = loader.get_template('account/profile.html')
        user = request.user
        context = {
            'endpoints': endpoints,
            'user': user,
        }
        return HttpResponse(template.render(context, request))
    return JsonResponse(status.data)


