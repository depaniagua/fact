from __future__ import unicode_literals

from django.db import models

from django.db import models
class Orden(models.Model):
    id= models.IntegerField
    descripcion= models.CharField(max_length=1000, null=True)
    proveedor = models.CharField(max_length=1000, null=True)
    costo= models.IntegerField (null=True)
