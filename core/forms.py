from django import forms
from django.forms import ModelForm
from .models import Vehiculo

# Formulario para crear (y editar) vehiculo
class VehiculoForm(ModelForm):
    class Meta:
        model  = Vehiculo
        fields = ['patente', 'marca', 'modelo', 'categoria'] 

