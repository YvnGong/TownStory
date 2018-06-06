from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.db import models
from django.contrib.auth.models import BaseUserManager

class City(models.Model):
    cityName = models.CharField(max_length = 30)
    stateName = models.CharField(max_length = 30)
    countryName = models.CharField(max_length = 30)

class Story(models.Model):
    city = models.ForeignKey(City, on_delete=models.CASCADE)