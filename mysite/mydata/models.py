# -*- coding: utf-8 -*-
from django.db import models
import time
from django.core.urlresolvers import reverse



# Create your models here.

class Customer(models.Model):
    PERSON = u'个人'
    BUSINESS = u'企业'
    CUSTOMERTYPE_CHOICES = (
        (PERSON, PERSON),
        (BUSINESS, BUSINESS),
    )
    customerType = models.CharField(u'客户类型', choices=CUSTOMERTYPE_CHOICES, default=PERSON,max_length=5)
    companyName = models.CharField(u'公司名称', primary_key=True, max_length=30)
    contactName = models.CharField(u'联系人名称', max_length=10)
    contactAddr = models.CharField(u'联系地址', max_length=30)
    contactTell = models.CharField(u'联系电话', max_length=30)

    class Meta:
        ordering = ['companyName']

    def __unicode__(self):
        return self.companyName


"""
设备类型model
"""


class DevType(models.Model):
    devType = models.CharField(u'设备类型', max_length=10, primary_key=True)
    devPart = models.CharField(u'所属部门', max_length=30)

    class Meta:
        ordering = ['devType']

    def __unicode__(self):
        return self.devType


class DevInfo(models.Model):
    devID = models.CharField(u'设备ID',primary_key=True, max_length=10)
    devType = models.ForeignKey(DevType,verbose_name=u'设备类型')
    isSale = models.BooleanField(u'是否卖出',default=False)
    isPass = models.BooleanField(u'是否通过检验',default=False)

    class Meta:
        ordering = ['devID']

    def __unicode__(self):
        return self.devID


class SaleInfo(models.Model):
    saleID = models.CharField(primary_key=True, max_length=20)
    saleTime = models.TimeField(verbose_name=u"销售时间", default=time.time())
    buyer = models.ForeignKey(Customer,verbose_name=u'购买方')
    devType = models.ForeignKey(DevType,verbose_name=u'设备类型')  # 这里是应该是表明这个订单是那个类型机器
    devID = models.TextField(u'销售设备ID',blank=False)  # 这里是这个订单中所有的设备ID，这里回事view的时候获取到选择的设备ID

    class Meta:
        ordering = ['saleID']

    def __unicode__(self):
        return self.saleID


class Fault(models.Model):
    faulltID=models.IntegerField(u'故障源ID',unique=True)
    faullt = models.CharField(u'故障源',max_length=50, primary_key=True)

    def __unicode__(self):
        return self.faullt

class Maintenance(models.Model):
    maintenanceID = models.CharField(u'维修ID',primary_key=True,max_length=10)
    devId = models.ForeignKey(DevInfo, verbose_name=u"设备ID")
    inputTime = models.DateTimeField(auto_now=True,verbose_name=u'录入时间')
    maintenanceTime = models.DateTimeField(verbose_name=u"维修时间")
    statu = models.CharField(u"维修状态", max_length=2)
    company = models.ForeignKey(Customer, verbose_name=u"所属公司")
    addr = models.CharField(u"维修地址", max_length=40)
    fault = models.ForeignKey(Fault, verbose_name=u"故障源")
    maintenancer = models.CharField(u"维修人员", max_length=10)  # 这里可能会成为一个外键
    detail = models.TextField(u'详细信息')
    part = models.TextField(u"更换工件", null=True)

    class Meta:
        ordering=['maintenanceID']

    def __unicode__(self):
        return self.maintenanceID

    def get_absolute_url(self):
        return reverse('wx',args=(self.devId,))

