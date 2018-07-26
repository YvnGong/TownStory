"""SmileyAppBackend URL Configuration
"""
from django.contrib import admin
from django.urls import path, include

# add favicon redirect
# from .settings import STATIC_URL
# from django.views.generic.base import RedirectView

#Jun10 new add sign in build in tool
from django.conf.urls import url
from django.contrib.auth import views as auth_views
#end
                       
urlpatterns = [
    path('', include('App.urls'), name='home'),
    path('app/', include('App.urls'), name='home_app'),
    path('admin/', admin.site.urls),
    url(r'^login/$', auth_views.login, name='login'),
    url(r'^logout/$', auth_views.logout, name='logout'),
    # for `allauth`
    url(r'^accounts/', include('allauth.urls')), 
    # for favicon
    # path('favicon.ico', RedirectView.as_view(url=STATIC_URL + 'image/favicon.ico')),
]
