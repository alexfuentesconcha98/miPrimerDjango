from django.shortcuts import render
from .serializers import VehiculoSerializer
from core.models import Vehiculo
from rest_framework.response import Response
from rest_framework.parsers import JSONParser
from rest_framework import status
from rest_framework.decorators import api_view 
# Create your views here.
def vehiculos(request):
    #lista todos los vehiculos
    if request.method == 'GET':
        vehiculos_lista = Vehiculo.objects.all()
        serializer = VehiculoSerializer(vehiculos_lista, many=True)
        return Response(serializer.data) 
    # Agrega vehiculo
    elif request.method == 'POST':
        data = JSONParser().parset(request)
        serializer = VehiculoSerializer(dato=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)    

