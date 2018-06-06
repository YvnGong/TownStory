import json
import os
from django.http import JsonResponse, HttpResponse
from django.contrib.auth.decorators import login_required
from django.template import Context, Template
from django.contrib.auth import authenticate, login
from django.views.decorators.csrf import csrf_exempt

from App.Utilities import S3Access
from pyReturn.response import status_response as sr

def landing(request):
    d = {
        'data': 1234,
        'status': True
    }
    return JsonResponse(d)

def auth(request):
    return HttpResponse('auth')

def city(request):
    return HttpResponse('city')

def story(request):
    return HttpResponse('story')

def write(request):
    return HttpResponse('write')

@csrf_exempt
def uploadImg(request):
    status = sr()
    file = None
    print(request.POST)
    print(request.FILES)
    if request.method == 'POST':
        image = request.FILES['image']
        url = S3Access.upload_file('fairytaler', image.file)
    status.attach_data('url', url, True)
    print(status.get_response())
    return JsonResponse(status.data)

@csrf_exempt
def uploadImgURL(request):
    status = sr()
    if request.method == 'GET':
        uploadURL, accessURL = S3Access.generate_presigned_upload_url('fairytaler')
    status.attach_data('uploadURL', uploadURL, True)
    status.attach_data('accessURL', accessURL, True)
    print(status.get_response())
    return JsonResponse(status.data)

@csrf_exempt
def uploadImgURLs(request):
    status = sr()
    if request.method == 'GET':
        imageCount = request.GET.get('imageCount')
        uploadURLs = []
        accessURLs = []
        for i in range(int(imageCount)):
            uploadURL, accessURL = S3Access.generate_presigned_upload_url('fairytaler')
            uploadURLs.append(uploadURL)
            accessURLs.append(accessURL)
    status.attach_data('uploadURLs', uploadURLs, True)
    status.attach_data('accessURLs', accessURLs, True)
    print(status.get_response())
    return JsonResponse(status.data)

@csrf_exempt
def uploadArticle(request):
    status = sr()
    if request.method == 'POST':
        title = request.POST.get('title')
        summary = request.POST.get('summary')
        article = request.POST.get('article')
        city = request.POST.get('city')
    print(title)
    print(summary)
    print(city)
    print(article)
    return JsonResponse(status.data)
