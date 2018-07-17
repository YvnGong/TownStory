from django.contrib import admin
from .models import City, Story, Like
# Register your models here.
admin.site.register(City)
admin.site.register(Story)
admin.site.register(Like)