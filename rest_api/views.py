from django.shortcuts import render
from .serializers import VehiculoSerializer
from core.models import Vehiculo
from rest_framework.response import Response
from rest_framework.parsers import JSONParser
from rest_framework import serializers, status
from rest_framework.decorators import api_view
#from rest_framework.decorators.csrf import csrf_exempt
# Create your views here.
#@csrf_exempt
@api_view(['GET','POST'])
def vehiculos(request):
    # lista todos los vehiculos
    if request.method == 'GET':
        vehiculos_lista = Vehiculo.objects.all()
        serializer = VehiculoSerializer(vehiculos_lista, many=True)
        return Response(serializer.data) 
    # Agrega vehiculo
    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = VehiculoSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST) 

@api_view(['GET', 'PUT', 'DELETE'])
def vehiculo(request, pk):
    # Instanciar el elemento singular desde la base de datos
    try:
        vehiculo = Vehiculo.objects.get(patente=pk)
    except Vehiculo.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method == 'GET':
        # Retornar un elemento vehiculo desde la bd
        serializer = VehiculoSerializer(vehiculo)
        return Response(serializer.data)
    if request.method == 'PUT':
        # Actualiza los datos de un elemento vehiculo en la bd
        data = JSONParser().parse(request)
        serializer = VehiculoSerializer(vehiculo, data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=status.HTTP_404_BAD_REQUEST)         
    elif request.method == 'DELETE':
        # Elimina un elemento vehiculo de la base de datos
        vehiculo.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)            
