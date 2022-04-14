from django.shortcuts import render
from django.contrib import auth
from django.contrib.auth import logout
from django.contrib.auth.models import Group
from django.contrib.auth.models import User
from django.contrib.auth.admin import UserAdmin
from django.shortcuts import render, redirect

from django.http import HttpResponseRedirect
# Create your views here.
def home_view(request):
    if request.user.is_authenticated:
        return HttpResponseRedirect('login')
    return render(request,'homePage.html')

def afterlogin(request):
    if request.user.is_authenticated == False:
        print("asdasdsadasdas")
        if request.method == 'POST':
            username = request.POST['username']
            password = request.POST.get('password1')
            user = auth.authenticate(username=username, password=password)
            if user.is_staff:
                auth.login(request, user)
                return redirect('HomePageadmin')





    else:
        if  request.user.is_staff:
            return redirect('HomePageadmin')
