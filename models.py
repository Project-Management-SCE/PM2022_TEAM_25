# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from contextlib import nullcontext
from operator import mod


from django.db import models


# Create your models here.

class passengers(models.Model):
    id = models.CharField(max_length=9, null=False,primary_key=True)
    fn = models.CharField(max_length=20, null=False)
    ln = models.CharField(max_length=20, null=False)
    email = models.CharField(max_length=40, null=False)
    phone = models.CharField(max_length=14, null=False)
    gender = models.CharField(max_length=5, null=False, default="male")
    age = models.DateField(null=False,default="01/01/2004")
    password = models.CharField(max_length=20,null=True)
    country=models.CharField(max_length=100, null=False,default="country")


class orders(models.Model):
    Chair=models.CharField(max_length=1000,null=True,default="chair")
    Food =models.CharField(max_length=100, null=True,default="Food")
    Cold =models.CharField(max_length=100, null=True,default="Cold drink")
    Hot =models.CharField(max_length=100, null=True,default="Hot drinks")
    Food =models.CharField(max_length=1000,null=True,default="nothing")
    



from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    email_confirmed = models.BooleanField(default=False)
    # other fields...












