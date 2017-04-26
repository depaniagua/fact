from __future__ import unicode_literals

from django.db import models

from django.db import models
class Orden(models.Model):
    #numero = models.IntegerField
    descripcion= models.CharField(max_length=1000)