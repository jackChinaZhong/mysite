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


urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    #url(r'^data/',include('mydata.urls')),
    url(r'^index/','mydata.views.index',name='index'),
    url(r'^customer/','mydata.views.newcustomer',name='add'),
    url(r'^type/','mydata.views.newdevtype',name='newdevtype'),
    url(r'^devinfo/','mydata.views.newdevinfo',name='newdevinfo'),
    url(r'^fault/','mydata.views.newfault',name='newfault'),
    url(r'^maintenance/','mydata.views.newmaintenance',name='newmaintenance'),
    url(r'^findCustomer/$','mydata.views.findcustomer',name='findcustomer'),
    url(r'^findDevinfo/$','mydata.views.findDevinfo',name='findDevinfo'),
    url(r'^saleinfo/$','mydata.views.index',name='saleinfo'),
    url(r'^qa/$','mydata.views.index',name='qa'),
    url(r'^wx/$','mydata.views.findMaintenance',name='wx'),
    url(r'^produce/$','mydata.views.index',name='produce'),
]
