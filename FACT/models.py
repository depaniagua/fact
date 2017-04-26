from __future__ import unicode_literals

from django.db import models

from django.db import models
class Orden(models.Model):
    descripcion= models.CharField(max_length=1000)
    cantidad = models.IntegerField
