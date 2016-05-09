from rest_framework import serializers
from django.contrib.auth.models import User, Group

class DevinfoSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model=User
        fields=('url','username','email','groups')
