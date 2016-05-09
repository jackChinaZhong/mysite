from django.conf.urls import url
from . import views

urlpatterns=[
    url(r'^addCustomer',views.newcustomer,name='add'),
    ]
