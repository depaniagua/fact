import datetime
from .models import Orden
from django.shortcuts import render
from rest_framework import generics
from rest_framework import viewsets
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser

from .models import Orden
from .serializers import OrdenSerializer
from rest_framework import generics


def index(request):
    lista_imagenes = Orden.objects.all()
    context = {'lista_imagenes': lista_imagenes}
    return render(request, 'fact/index.html', context)

@csrf_exempt
def orden(request):
    if request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = OrdenSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)


def crearOrden(request):
    return render(request, 'fact/orden/agregarOrden.html')
