# -*- coding:utf-8 -*-
from django.shortcuts import render, HttpResponseRedirect
# Create your views here.
from models import *
from forms import *
import time
import datetime
import django.utils.timezone as timezone
from django.http import Http404, HttpResponse

from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from serializers import  *


# 这里是主界面
def index(request):
    return render(request, "mydata/home.html")


def newcustomer(request):
    if request.method == 'POST':
        form = CustomerForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/index/')
    else:
        form = CustomerForm()
    return render(request, "mydata/addCustomer.html", {'form': form})


def newdevtype(request):
    if request.method == 'POST':
        form = DevTypeForm(request.POST)
        if form.is_valid():
            form.save()
        return HttpResponseRedirect('/index/')
    else:
        form = DevTypeForm()
    return render(request, "mydata/addDevtype.html", {'form': form})


def newdevinfo(request):
    if request.method == 'POST':
        form = DevInfoForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = DevInfoForm()

    return render(request, "mydata/addDevinfo.html", {'form': form})


def newSaleInfo(request):
    return render(request, "mydata/addSaleInfo.html")


def newfault(request):
    if request.method == 'POST':
        form = FaultForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = FaultForm()
    return render(request, "mydata/addFault.html", {'form': form})


def newmaintenance(request):
    if request.method == 'POST':
        form = MaintenanceForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.maintenanceTime = timezone.now()
            post.save()
    else:
        form = MaintenanceForm()
    return render(request, "mydata/addMaintenance.html", {'form': form})


def findcustomer(request):
    statu = None
    customertype_list = Customer.objects.values_list('customerType', flat=True).distinct()

    query_customertype = request.GET.get('customerType', 'all')
    if (not query_customertype) or Customer.objects.filter(customerType=query_customertype).count() is 0:
        query_customertype = 'all'
        customer_list = Customer.objects.all()
    else:
        customer_list = Customer.objects.filter(customerType=query_customertype)

    if request.method == 'POST':
        keyword = request.POST.get('keyword', '')
        customer_list = Customer.objects.filter(companyName__contains=keyword)
        query_customertype = 'all'

    content = {
        'user': request.user,
        'active_menu': 'findCustomer',
        'customertype_list': customertype_list,
        'customer_list': customer_list,
        'state': statu,
    }
    return render(request, 'mydata/findCustomer.html', content)


# 这里是通过设备ID来查询，也可以提供一个维修ID来查询
def findMaintenance(request):
    devid = request.GET.get('devid', '')
    maintenance_list = None
    error = False
    emessage = ""
    QueryDevID=True
    if devid.isalnum and devid !="":
        try:
            devinfo=DevInfo.objects.get(devID=devid)
            maintenance_list = Maintenance.objects.filter(devId=devinfo)
            if  not maintenance_list:
                error=True
                QueryDevID = True
                emessage=u"此设备ID无维护信息"
        except DevInfo.DoesNotExist:
            error = True
            emessage = u"设备ID不存在"
    else:
        maintenanceid = request.GET.get('wxid', '')
        QueryDevID = False
        if maintenanceid.isalnum:
            try:
                maintenance_list = Maintenance.objects.get(maintenanceID=maintenanceid)
            except Maintenance.DoesNotExist:
                error = True
                emessage = u"维修单号错误"
    content = {
        'form': maintenance_list,
        'error': error,
        'querid':QueryDevID,
        'message': emessage,
    }
    return render(request, 'mydata/findMaintenance.html', content)


"""
如何计算出设备维护信息，设备销售，生产，质检的url并返回
"""


def findDevinfo(request):
    devmodel_list = ((u'销售', 'saleinfo'), u'质检', u'维护', u'生产')
    devmode_list = ({u'销售信息': 'saleinfo'}, {u'质检信息': 'qa'}, {u'维护信息': 'wx'}, {u'生产信息': 'produce'})
    devtype_list = DevType.objects.all()  # 查询设备类型列表
    devinfo_list = DevInfo.objects.all()
    # 这里是输入一个关键字的时候获取设备ID包含这个关键字
    if request.method == 'POST':
        keyword = request.POST.get('keyword', '')
        if keyword.isalnum:
            devinfo_list = DevInfo.object.filter(devID__contains=keyword)
    content = {
        'user': request.user,
        'devmode_list': devmode_list,
        'devtype_list': devtype_list,
        'devinfo_list': devinfo_list,
    }
    return render(request, 'mydata/findDevinfo.html', content)



class UserViewSet(viewsets.ModelViewSet):
    queryset=User.objects.all()
    serializer_class = DevinfoSerializer