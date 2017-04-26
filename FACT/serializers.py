from django.contrib.auth.models import User, Group
from rest_framework import serializers

from .models import Orden

class OrdenSerializer(serializers.ModelSerializer):
    class Meta:
        model = Orden
        #fields = ('id','proveedor')
        fields = ('cantidad','descripcion')
