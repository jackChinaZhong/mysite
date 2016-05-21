#coding:utf-8
from django import forms
from models import *
from django.forms import ModelForm
import re

Rmath = r'((\d{11})|^((\d{7,8})|(\d{4}|\d{3})-(\d{7,8})|(\d{4}|\d{3})-(\d{7,8})-(\d{4}|\d{3}|\d{2}|\d{1})|(\d{7,8})-(\d{4}|\d{3}|\d{2}|\d{1}))$)'

class CustomerForm(ModelForm):
    def clean_contactTell(self):
        data = self.cleaned_data['contactTell']
        if not re.match(data, Rmath):
            raise forms.ValidationError(u'电话号码格式输入错误')
        return data

    class Meta:
        model=Customer
        fields=('customerType','companyName','contactName','contactAddr','contactTell')

class DevTypeForm(ModelForm):
    class Meta:
        model=DevType
        fields=('devType','devPart')

class DevInfoForm(ModelForm):
    class Meta:
        model=DevInfo
        fields=('devID','devType')

class FaultForm(ModelForm):
    class Meta:
        model=Fault
        fields=('faulltID','faullt')

class MaintenanceForm(ModelForm):
    class Meta:
        model=Maintenance
        fields=('maintenanceID','devId','maintenanceTime','statu','company','addr','fault',
                'maintenancer','detail','part')
class pipelineOneForm(ModelForm):
    class Meta:
        model = pipelineOne
        exclude = ['ProductionDate']


class piplineTwoForm(ModelForm):
    class Meta:
        model = pipelineTwo
        exclude = ['ProductionDate']


class piplineThreeForm(ModelForm):
    class Meta:
        model = pipelineThree
        exclude = ['ProductionDate']

class piplineFourForm(ModelForm):
    class Meta:
        model = pipelineFour
        exclude = ['ProductionDate']


class piplineFiveForm(ModelForm):
    class Meta:
        model = pipelineFive
        exclude = ['ProductionDate']
