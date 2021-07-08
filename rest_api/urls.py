from django.urls import path
from rest_api.views import vehiculos

urlpatterns = [
    path('vehiculos/', vehiculos, name='vehiculos'),
]