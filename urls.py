"""PassengerWebsite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
#from . import views
from paSSengersformes.views import Index,signup,Homepage,Indexes,forgot,Orders,show,rating





urlpatterns = [
    path('admin/', admin.site.urls),
    path('',Homepage,name="home"),
    path('register/',signup,name="signup"),
    path('login/', Index,name="login"),
    path('login/Indexes/', Indexes,name="Indexes"),
    path('login/register/',signup,name="signup"),
    path('login/forgot/',forgot,name="forgot"),
    path('login/Indexes/home/',Homepage,name="home"),
    path('login/Indexes/orders/',Orders,name="orders"),
    path('login/Indexes/show/',show,name="show"),
    path('login/Indexes/rating/',rating,name="rating"),


]



from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns += staticfiles_urlpatterns()













