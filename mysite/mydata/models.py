# -*- coding: utf-8 -*-
from django.db import models
import time


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
    #maintenanceTime = models.DateField(verbose_name=u"维修时间")
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

class pipelineOne(models.Model):
    COMPLETE = u'完成'
    UNFIT = u'不适合'
    CHOICES = (
        (COMPLETE, COMPLETE),
        (UNFIT, UNFIT),
    )

    #devID = models.ForeignKey(DevInfo, unique=True,verbose_name=u'产品编号')
    devID = models.OneToOneField(DevInfo, verbose_name=u'产品编号')
    # devID=models.CharField(u'产品编号',primary_key=True)
    QuickPlug = models.CharField(u'快速插座', choices=CHOICES, max_length=6)
    FBIC = models.CharField(u'平底隔离柱', choices=CHOICES, max_length=6)
    Coil = models.CharField(u'过线圈', choices=CHOICES, max_length=6)
    DPRP = models.CharField(u'拖板与加强板', choices=CHOICES, max_length=6)
    OutputFilter = models.CharField(u'输出滤波板', choices=CHOICES, max_length=6)
    MainTransformer = models.CharField(u'主变压器', choices=CHOICES, max_length=6)
    TCRWithPin = models.CharField(u'电抗器安装与引脚接线', choices=CHOICES, max_length=6)
    ControlTransformer = models.CharField(u'控制变压器', choices=CHOICES, max_length=6)
    Bridge = models.CharField(u'整流桥', choices=CHOICES, max_length=6)
    EarthStud = models.CharField(u'接地螺栓', choices=CHOICES, max_length=6)
    AluPlateAndBasePlate = models.CharField(u'铝隔板与底板', choices=CHOICES, max_length=6)
    BridgeHeatSink = models.CharField(u'整流桥散热器', choices=CHOICES, max_length=6)
    OutputProtectionRe = models.CharField(u'输出保护电阻', choices=CHOICES, max_length=6)
    cap = models.CharField(u'电容(20UF/650v)', choices=CHOICES, max_length=6)
    Assembling = models.CharField(u'装配人', max_length=10)
    ProductionDate = models.DateField(auto_now=True, verbose_name=u'生产日期')

    class Meta:
        ordering = ['devID']

    def __unicode__(self):
        return self.devID


class pipelineTwo(models.Model):
    COMPLETE = u'完成'
    UNFIT = u'不适合'
    CHOICES = (
        (COMPLETE, COMPLETE),
        (UNFIT, UNFIT),
    )
    ELECAPCOMMODEL = (
        ('DCMEC 2200uF/400V', 'DCMEC 2200uF/400V'),
        ('DCMEC 1000uF/400V', 'DCMEC 1000uF/400V'),
        ('50uF/500V', '50uF/500V'),
    )
    ELECAPCOMMAKER = (
        (u'CDE', u'CDE'),
        (u'江海', u'江海'),
        (u'信达', u'信达'),
        (u'方华', u'方华'),
        (u'宏峰', u'宏峰'),
    )
    BLOCKCAP = (
        ('4uF/1KV', '4uF/1KV'),
        ('5uF/1KV', '5uF/1KV'),
        ('6uF/1KV', '6uF/1KV'),
        ('8uF/1KV', '8uF/1KV'),
    )
    IGBTMODEL = (
        ('FF150R12KS4', 'FF150R12KS4'),
        ('FF100R12KS4', 'FF100R12KS4'),
        ('SKM100GB128D', 'SKM100GB128D'),
        ('SKM75GB128D', 'SKM75GB128D'),
        ('GD100HFV12C8S', 'GD100HFV12C8S'),
        ('GD75HFV12C8S', 'GD75HFV12C8S'),
    )
    IGBTMAKER = (
        (u'西门子', u'西门子'),
        (u'西门康', u'西门康'),
        (u'斯达', u'斯达'),
    )
    DIODEMODEL = (
        ('MMF200ZB040DK1', 'MMF200ZB040DK1'),
        ('DH2F100N4S', 'DH2F100N4S'),
        ('MURL20056CT', 'MURL20056CT'),
    )
    DIODEMAKER = (
        (u'江苏宏微', u'江苏宏微'),
        (u'大伟', u'大伟'),
        (u'大科', u'大科')
    )
    SENSORMODEL = (
        ('L03S400D15WM', 'L03S400D15WM'),
        ('TBC300BA', 'TBC300BA'),
        ('HAS400-S/S950', 'HAS400-S/S950'),
        ('TBC300BA', 'TBC300BA'),
    )
    SENSORMAKER = (
        (u'日本田村', u'日本田村'),
        (u'莱姆', u'莱姆'),
        (u'拓肯', u'拓肯')
    )
    CONTROTRANSFROMERMAKER = (
        (u'绵阳天意电子有限公司', u'绵阳天意电子有限公司'),
        (u'绵阳宇虹电子有限公司', u'绵阳宇虹电子有限公司'),
    )
    #devID = models.ForeignKey(DevInfo, verbose_name=u'产品编号')
    devID = models.OneToOneField(DevInfo, verbose_name=u'产品编号')
    EleCapCom = models.CharField(u'电解电容组合', max_length=6, choices=CHOICES)
    EleCapComModel = models.CharField(u'电解电容型号', max_length=20, choices=ELECAPCOMMODEL)
    EleCapComMaker = models.CharField(u'电解电容厂家', max_length=10, choices=ELECAPCOMMAKER)
    BlockCap = models.CharField(u'隔直电容', max_length=10, choices=BLOCKCAP)
    IGBTSINK = models.CharField(u'IGBT散热器', max_length=6, choices=CHOICES)
    IGBTModel = models.CharField(u'IGBT模块型号', max_length=20, choices=IGBTMODEL)
    IGBTMaker = models.CharField(u'IGBT厂家', max_length=10, choices=IGBTMAKER)
    DiodeHeatSink = models.CharField(u'二极管模块散热器', max_length=6, choices=CHOICES)
    DiodeModel = models.CharField(u'二极管模块型号', max_length=15, choices=DIODEMODEL)
    DiodeMaker = models.CharField(u'二极管模块厂家', max_length=10, choices=DIODEMAKER)
    Cap = models.CharField(u'电容20uF/650V', max_length=6, choices=CHOICES)
    OutputCopper = models.CharField(u'输出铜排', max_length=6, choices=CHOICES)
    SensorModel = models.CharField(u'传感器型号', max_length=20, choices=SENSORMODEL)
    SensorMaker = models.CharField(u'传感器厂家', max_length=20, choices=SENSORMAKER)
    TransformerSecSideWiring = models.CharField(u'主变压器副边接线', max_length=6, choices=CHOICES)
    TransformerPriSideWiring = models.CharField(u'主变压器原边接线', max_length=6, choices=CHOICES)
    PhaseInduConnection = models.CharField(u'移相电感接线', max_length=6, choices=CHOICES)
    CommutationInductor = models.CharField(u'换流电感安装与接线', max_length=6, choices=CHOICES)
    ControTransformer = models.CharField(u'控制变压器', max_length=6, choices=CHOICES)
    ControTransformerMaker = models.CharField(u'控制变压器厂家', max_length=20, choices=CONTROTRANSFROMERMAKER)
    Assembling = models.CharField(u'装配人', max_length=10)
    ProductionDate = models.DateField(auto_now=True, verbose_name=u'生产日期')

    class Meta:
        ordering = ['devID']

    def __unicode__(self):
        return self.devID


class pipelineThree(models.Model):
    COMPLETE = u'完成'
    UNFIT = u'不适合'
    CHOICES = (
        (COMPLETE, COMPLETE),
        (UNFIT, UNFIT),
    )
    """
    风机型号,风机生产商,数显表型号,数显表厂家
    """
    FANMODEL = (
        ('200FZY7-D', '200FZY7-D'),
    )
    FANMAKER = (
        (u'苏州电讯', u'苏州电讯'),
    )
    DIGITAL = (
        ('PZ50-A13', 'PZ50-A13'),
        ('1111-4', '1111-4'),
    )
    DIGITALMAKER = (
        (u'苏州横河', u'苏州横河'),
        (u'上海瀚显', u'上海瀚显'),
        (u'成都熊谷', u'成都熊谷'),
    )
    #devID = models.ForeignKey(DevInfo, verbose_name=u'产品编号')
    devID = models.OneToOneField(DevInfo, verbose_name=u'产品编号')
    IGBTConnectionAndAB = models.CharField(u'IGBT接线与AB保护板', choices=CHOICES, max_length=6)
    FrontAndRearPanels = models.CharField(u'前,后面板', max_length=6)
    Fan = models.CharField(u'风机型号', choices=FANMODEL, max_length=20)
    fanmaker = models.CharField(u'风机厂家', choices=FANMAKER, max_length=20)
    DigitalModel = models.CharField(u'数显表型号', choices=DIGITAL, max_length=20)
    digitalmaker = models.CharField(u'数显表厂家', choices=DIGITALMAKER, max_length=20)
    IGBTPIN = models.CharField(u'IGBT接线', choices=CHOICES, max_length=6)
    TenCoreAirOutlet = models.CharField(u'十芯航空插座', choices=CHOICES, max_length=6)
    Assembling = models.CharField(u'装配人', max_length=10)
    ProductionDate = models.DateField(auto_now=True, verbose_name=u'生产日期')

    class Meta:
        ordering = ['devID']

    def __unicode__(self):
        return self.devID


class pipelineFour(models.Model):
    COMPLETE = u'完成'
    UNFIT = u'不适合'
    CHOICES = (
        (COMPLETE, COMPLETE),
        (UNFIT, UNFIT),
    )
    ARISWITCHMODEL = (
        ('NDM1-63 C50', 'NDM1-63 C50'),
        ('NDM1-63 C40', 'NDM1-63 C40'),
        ('BM-63 50A', 'BM-63 50A'),
        ('BM-63 40A', 'BM-63 40A'),
    )
    ARISWITCHMAKER = (
        (u'上海良信电器股份有限公司', u'上海良信电器股份有限公司'),
        (u'台安科技(无锡)', u'台安科技(无锡)'),
    )
    #devID = models.ForeignKey(DevInfo, verbose_name=u'产品编号')
    devID = models.OneToOneField(DevInfo, verbose_name=u'产品编号')
    EnterFilterInductor = models.CharField(u'输入滤波电感', choices=CHOICES, max_length=6)
    WholeWiring = models.CharField(u'整机接线', choices=CHOICES, max_length=6, default=COMPLETE)
    AriSwitchBracket = models.CharField(u'空气开关支架', choices=CHOICES, max_length=6)
    AriSwitchModel = models.CharField(u'空气开关型号', choices=ARISWITCHMODEL, max_length=10)
    AriSwitchMaker = models.CharField(u'空气开关厂家', choices=ARISWITCHMAKER, max_length=20)
    EnterFilterPlate = models.CharField(u'输入滤波板', choices=CHOICES, max_length=6)
    Assembling = models.CharField(u'装配人', max_length=10)
    ProductionDate = models.DateField(auto_now=True, verbose_name=u'生产日期')

    class Meta:
        ordering = ['devID']

    def __unicode__(self):
        return self.devID


class pipelineFive(models.Model):
    COMPLETE = u'完成'
    UNFIT = u'不适合'
    CHOICES = (
        (COMPLETE, COMPLETE),
        (UNFIT, UNFIT),
    )
    #devID = models.ForeignKey(DevInfo, verbose_name=u'产品编号')
    devID = models.OneToOneField(DevInfo, verbose_name=u'产品编号')
    ControlPanel = models.CharField(u'控制板', choices=CHOICES, max_length=6)
    ControlPanelVersion = models.CharField(u'控制板版本号', max_length=10)
    CarriageAndBracingSheet = models.CharField(u'拖板与加强板', max_length=6, choices=CHOICES)
    Bundle = models.CharField(u'扎线', max_length=6, choices=CHOICES)
    caulking = models.CharField(u'打胶', max_length=6, choices=CHOICES)
    Assembling = models.CharField(u'装配人', max_length=10)
    ProductionDate = models.DateField(auto_now=True, verbose_name=u'生产日期')

    class Meta:
        ordering = ['devID']

    def __unicode__(self):
        return self.devID
