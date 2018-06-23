from django.urls import path
from . import views

urlpatterns = [
    path('', views.landPage_Tester, name = 'landing'),
    path('authenticate', views.auth, name = 'auth'),
    path('city', views.city, name = 'city'),
    path('story', views.story, name = 'story'),
    path('write', views.write, name = 'write'),
    path('uploadImg', views.uploadImg, name = 'uploadImg'),
    path('uploadImgURL', views.uploadImgURL, name = 'uploadImgURL'),
    path('uploadImgURLs', views.uploadImgURLs, name = 'uploadImgURLs'),
    path('uploadArticle', views.uploadArticle, name = 'uploadArticle'),
    path('getStory', views.getStory, name = 'getStory'),
    path('test', views.test, name='test'),
    path('about', views.about, name='about'),
    path('contact', views.contact, name='contact'),
    path('map', views.map, name='map'),
    # path('login', views.Login_Tester, name = 'login')

]

