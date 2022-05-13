import re
import urllib

from django.contrib import auth
from django.contrib.auth import logout
from django.contrib.auth.models import Group
from travil.models import orders
from django.contrib.auth.models import User
from django.contrib.auth.admin import UserAdmin
from django.shortcuts import render, redirect
from travil import forms
from django.http import HttpResponseRedirect


def login(request):
    # if request.user.is_authenticated:
    #     return HttpResponseRedirect('login')
    return render(request,'index.html')



def home(request):
    if request.user.is_authenticated == False:
        print("asdasdsadasdas")
        if request.method == 'POST':
            username = request.POST['username']
            password = request.POST.get('password1')
            user = auth.authenticate(username=username, password=password)
            
            if user is not None and user.groups.filter(name='WORKER').exists():
                auth.login(request, user)
                return redirect('Indexes')

    else:
        if  request.user.is_staff:
            return redirect('HomePageadmin')
        elif request.user.groups.filter(name='WORKER'):
            return redirect('homePageWorker')
     


def logout(request):
    return render(request,'index.html')




def homePageWorker(request):
    return render(request,'homePageWorker.html')



def forgot(request):
    return render(request,"forgot.html")







def About(request):
    return render(request, 'About.html')

def Indexes(request):
     url = 'https://data.gov.il/api/3/action/datastore_search?resource_id=e83f763b-b7d7-479e-b172-ae981ddc6de5&limit=5&q=title:jones'
     #url = "https://data.gov.il/api/3/action/datastore_search?resource_id=e83f763b-b7d7-479e-b172-ae981ddc6de5&limit=5"
     fileobj = urllib.request.urlopen(url)
     fileobj = fileobj.read()
     return render(request, 'Indexes.html',{"data":fileobj})


def orders(request):
    if request.method == 'POST':
        cold1 = request.POST['cold']
        hot1 = request.POST['hot']
        food1 = request.POST['food']
        other1 = request.POST['other']

   # orders.objects.create(cold=cold1,hot=hot1,food=food1,other=other1)
  #  orders.save()


    return render(request, 'orders.html')

def home(request):
    return render(request,'Indexes.html')


def show(request):
    #ordered = orders.objects.all()
    return render(request,"show.html",{'orderd':orders})


def reports(request):
    if request.method == 'POST':
        fullname1 = request.POST['fullname']
        text1 = request.POST['text']

   # orders.objects.create(fullname=fullname1,text=text1)
  #  orders.save()
    return render(request,"reports.html")



def showre(request):
#ordered = orders.objects.all()
    return render(request,"showre.html",{'ordered':orders})



def show_schedule(request):
    #your = schedule.objects.all()
    #return render(request,"schedule.html",{'your':schedule})
    return render(request,'schedule.html')