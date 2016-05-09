from django import forms
from models import *
from django.forms import ModelForm

class CustomerForm(ModelForm):

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
        fields=('maintenanceID','devId','statu','company','addr','fault',
                'maintenancer','detail','part')
