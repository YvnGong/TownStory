"""SmileyAppBackend URL Configuration
"""
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('app/', include('App.urls')),
    path('admin/', admin.site.urls),
]
