# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import redirect, render

# Create your views here.
from Passenger.models import passengers

def login_page(request):
    message=''
    Lcounter=0
    Ncounter=0
    Scounter=0
    if request.method == 'POST':
        email = request.POST.get('email')
        p = request.POST.get('password')
        for i in p:
            print(ord(i))
            if ord(i) >= 97 and ord(i) <= 122:
                Lcounter = Lcounter + 1

            if ord(i) >= 48 and ord(i) <= 57:
                Ncounter = Ncounter + 1

            if ord(i) >= 33 and ord(i) <= 38:
                Scounter = Scounter + 1

            if (Lcounter == 0):
                message = 'The password most have letters!'

            if (Ncounter == 0):
                message = 'The password most have numbers!'

            if (Scounter == 0):
                message = 'The password most have Special letters!'

            if passengers.objects.filter(email=email, password=p).exists():
                return redirect('passenger')
            content = {'message': message}
            return render(request, 'index.html', content)

        # def signup(request):
        #     lst = register.objects.all()
        #     content = {'RegisterationForm': lst}
        #     return render(request, 'RegisterationForm.html', content)
    content = {}
    return render(request, 'index.html', content)


def Index(request):
    return render(request, 'index.html')

def signup(request):
    return render(request, 'register.html')