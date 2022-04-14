from django.shortcuts import render
from django.contrib import auth
from django.contrib.auth import logout
from django.contrib.auth.models import Group
from django.contrib.auth.models import User
from django.contrib.auth.admin import UserAdmin
from django.shortcuts import render, redirect

from django.http import HttpResponseRedirect
# Create your views here.
from Trival import forms


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
            elif user is not None and user.groups.filter(name='WORKER').exists():
                auth.login(request, user)
                return redirect('homePageWorker')




    else:
        if  request.user.is_staff:
            return redirect('HomePageadmin')
        elif request.user.groups.filter(name='WORKER'):
            return redirect('homePageWorker')


def logOut(request):
    logout(request)
    return redirect('workerlogin')

def worker_signup(request):
    userForm = forms.WorkerUserForm()
    workerForm = forms.WorkerForm()

    mydict = {'userForm': userForm, 'workerForm': workerForm}
    if request.method == 'POST':
        userForm = forms.WorkerUserForm(request.POST)
        workerForm = forms.WorkerForm(request.POST, request.FILES)
        print(workerForm.is_valid())
        if userForm.is_valid() and workerForm.is_valid():
            user = userForm.save()
            user.set_password(user.password)
            user.save()
            worker = workerForm.save(commit=False)
            worker.user = user
            worker.save()
            my_customer_group = Group.objects.get_or_create(name='WORKER')
            my_customer_group[0].user_set.add(user)
        return HttpResponseRedirect('workerlogin')
    return render(request, 'workersignup.html', context=mydict)


def HomePageadmin(request):
    return render(request,'HomePageadmin.html')