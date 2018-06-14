from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, User
from django.db import models
from django.contrib.auth.models import BaseUserManager
# time zone
from django.utils import timezone
# uuid
import uuid

"""
Potential User Profile
"""
# class Profile(models.Model):
#     user = models.OneToOneField(User, on_delete=models.CASCADE)
#     bio = models.TextField(max_length=500, blank=True)
#     location = models.CharField(max_length=30, blank=True)
#     birth_date = models.DateField(null=True, blank=True)

# @receiver(post_save, sender=User)
# def create_user_profile(sender, instance, created, **kwargs):
#     if created:
#         Profile.objects.create(user=instance)

# @receiver(post_save, sender=User)
# def save_user_profile(sender, instance, **kwargs):
#     instance.profile.save()

class City(models.Model):
    city = models.CharField(max_length = 50, primary_key = True, unique = True)
    city_name = models.CharField(max_length = 20)
    state_name = models.CharField(max_length = 20)
    country_name = models.CharField(max_length = 20)
    number_of_story = models.IntegerField(default=0)

class Story(models.Model):
    id = models.CharField(max_length = 50, primary_key = True, unique = True)
    city = models.ForeignKey(City, on_delete=models.CASCADE)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length = 50)
    summary = models.CharField(max_length = 150)
    cover = models.CharField(max_length = 50)
    like = models.IntegerField(default=0)
    date = models.DateField(default=timezone.now)