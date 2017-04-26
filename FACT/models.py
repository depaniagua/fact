from __future__ import unicode_literals

from django.db import models

from django.db import models
class Orden(models.Model):
    id= models.IntegerField
    descripcion= models.CharField(max_length=1000)
    proveedor = models.CharField(max_length=1000)
    costo= models.IntegerField
