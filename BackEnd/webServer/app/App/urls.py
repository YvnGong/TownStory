from django.urls import path
from . import views

urlpatterns = [
    path('', views.landing, name = 'landing'),
    path('healthcheck', views.healthcheck, name = 'landing'),
    path('city', views.city, name = 'city'),
    path('story', views.story, name = 'story'),
    path('deleteStory', views.deleteStory, name = 'deleteStory'),
    path('write', views.write, name = 'write'),
    path('uploadImg', views.uploadImg, name = 'uploadImg'),
    path('uploadImgURL', views.uploadImgURL, name = 'uploadImgURL'),
    path('uploadImgURLs', views.uploadImgURLs, name = 'uploadImgURLs'),
    path('uploadArticle', views.uploadArticle, name = 'uploadArticle'),
    path('about', views.about, name='about'),
    path('contact', views.contact, name='contact'),
    path('privacy_policy', views.privacy_policy, name='privacy_policy'),
    path('term_of_services', views.term_of_services, name='term_of_services'),
    path('discover', views.discover, name='discover'),
]

