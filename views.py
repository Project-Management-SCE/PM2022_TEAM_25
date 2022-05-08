# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import redirect, render
import urllib.request
# config={
#   'apiKey': "AIzaSyCJjemPvqf6u2EwqubIDC0sxPm6BOiaQSo",
#   'authDomain': "flyeasily-94233.firebaseapp.com",
#   'projectId': "flyeasily-94233",
#   'storageBucket': "flyeasily-94233.appspot.com",
#   'messagingSenderId': "1071401196458",
#   'appId': "1:1071401196458:web:1604cc5a773497ab3269d3",
#   'measurementId': "G-RHDYNGLNT1"
# }
# firebase=pyrebase.initialize_app(config)
# auth=firebase.auth()



# Create your views here.

def login_page(request):
    message=''
    Lcounter=0
    Ncounter=0
    #Scounter=0
    if request.method == 'POST':
        email = request.POST.get('email')
        p = request.POST.get('password')
        for i in p:
            print(ord(i))
            if ord(i) >= 97 and ord(i) <= 122:
                Lcounter = Lcounter + 1

            if ord(i) >= 48 and ord(i) <= 57:
                Ncounter = Ncounter + 1

            # if ord(i) >= 33 and ord(i) <= 38:
            #     Scounter = Scounter + 1

            if (Lcounter == 0):
                message = 'The password most have letters!'

            if (Ncounter == 0):
                message = 'The password most have numbers!'

            # if (Scounter == 0):
            #     message = 'The password most have Special letters!'

            if passengers.objects.filter(email=email, password=p).exists():
                return redirect('passengers')
            content = {'message': message}
            return render(request, 'index.html', content)




def Sign_up(request):
    content = {}
    lst = passengers.objects.all()
    content = {'RegisterationForm': lst}
    return render(request, 'signup.html', content)

def Home(request):
    content = {}
    lst = passengers.objects.all()
    content = {'RegisterationForm': lst}
    return render(request, 'home.html', content)

def Homepage(request):
    return render(request,'home.html')

def Index(request):
    return render(request, 'index.html')

def Signup(request):
    return render(request, 'signup.html')


def Indexes(request):
    url = 'https://data.gov.il/api/3/action/datastore_search?resource_id=e83f763b-b7d7-479e-b172-ae981ddc6de5&limit=90&q=title:jones'  
    #url = "https://data.gov.il/api/3/action/datastore_search?resource_id=e83f763b-b7d7-479e-b172-ae981ddc6de5&limit=5"
    yrl="https://data.gov.il/api/3/action/datastore_search?resource_id=e83f763b-b7d7-479e-b172-ae981ddc6de5&q=jones"
    fileobj = urllib.request.urlopen(yrl)
    fileobj = fileobj.read()
    return render(request, 'Indexes.html',{"data":fileobj})




def forgot(request):
    return render(request, 'forgot.html')