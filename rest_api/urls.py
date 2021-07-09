from django.urls import path
from rest_api.views import vehiculos, vehiculo

urlpatterns = [
    path('vehiculo/', vehiculos, name='vehiculos'),
    path('vehiculo/<pk>', vehiculo, name='vehiculo')
]