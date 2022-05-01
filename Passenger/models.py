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
    age = models.SmallIntegerField(null=False,default="18")
    password = models.CharField(max_length=20,null=True)
    country=models.CharField(max_length=20,null=False,default="country")










