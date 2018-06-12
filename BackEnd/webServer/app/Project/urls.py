"""SmileyAppBackend URL Configuration
"""
from django.contrib import admin
from django.urls import path, include

#Jun10 new add sign in build in tool
from django.conf.urls import url
from django.contrib.auth import views as auth_views
#end
                       
urlpatterns = [
    path('app/', include('App.urls'), name='home'),
    path('admin/', admin.site.urls),
    url(r'^login/$', auth_views.login, name='login'),
    url(r'^logout/$', auth_views.logout, name='logout'),
]
