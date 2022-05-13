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
    gender = models.CharField(max_length=50, null=False, default="male")
    age = models.DateField(null=False,default="01/01/2004")
    password1 = models.CharField(max_length=20,null=True)
    password2 = models.CharField(max_length=20,null=True)
    country=models.CharField(max_length=100, null=False,default="country")
    class Meta:  
        db_table = "passengers"  
    


class orders(models.Model):
    cold =models.CharField(max_length=100, null=True,default="Cold drink")
    hot =models.CharField(max_length=100, null=True,default="Hot drinks")
    chair=models.CharField(max_length=100,null=False,primary_key=True)
    food =models.CharField(max_length=100, null=True,default="Food")
    other =models.CharField(max_length=1000,null=True,default="nothing")
    class Meta:  
        db_table = "orders"  






class ratings(models.Model):
    name= models.CharField(max_length=20,null=True,default="name")
    worker=models.CharField(max_length=20,null=False,primary_key=True)
    rating=models.CharField(max_length=3,null=False,default="0")
    





