"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import include, url
from django.contrib import admin
from mydata import views
from mydata.views import *


urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^customer/', newcustomer, name='add'),
    url(r'^type/', newdevtype, name='newdevtype'),
    url(r'^devinfo/', newdevinfo, name='newdevinfo'),
    url(r'^fault/', newfault, name='newfault'),
    url(r'^maintenance/', newmaintenance, name='newmaintenance'),
    url(r'^findCustomer/$', findcustomer, name='findcustomer'),
    url(r'^findDevinfo/$', findDevinfo, name='findDevinfo'),
    url(r'^saleinfo/$', index, name='saleinfo'),
    url(r'^qa/$', index, name='qa'),
    url(r'^wx/$', findMaintenance, name='wx'),
    url(r'^produce/$', index, name='produce'),
    url(r'^postion1/$', addPipeLineOne, name='addPipeLineOne'),
    url(r'^postion2/$', addPipeLineTwo, name='addPipeLineOne'),
    url(r'^postion3/$', addPipeLineThree, name='addPipeLineOne'),
    url(r'^postion4/$', addPipeLineFour, name='addPipeLineOne'),
    url(r'^postion5/$', addPipeLineFive, name='addPipeLineOne'),
]
