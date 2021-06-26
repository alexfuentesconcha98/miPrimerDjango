from django.shortcuts import render, redirect
from .models import Vehiculo 
from .forms import VehiculoForm
# Create your views here.
#Se define clase(basica)

class Persona:
    def __init__(self,nombre,edad):
        self.nombre = nombre
        self.edad = edad
        super().__init__()

# Se define la funcion home en views.py para mostrar html home "python manage.py runserver"
def home(request):
    hijo = Persona("kity",'12')
    lista = ["chocolate", "pollo", "humitas"]
    contexto = {
        
        'nombre': ' Alex Fuentes Concha',
        'edad': 23,
        'comidas': lista,
        'hijo': hijo
    }
    return render(request, 'core/home.html', contexto)

def blog(request): 
    lista2 = ["gustavo","cristina" ]
    contexto = {
        
        'nombre': ' Alex Fuentes Concha',
        'edad': 23,
        'nombres': lista2
    }
    return render(request, 'core/blog.html', contexto)

def  blog2(request):
    
    return render(request,'core/blog2.html')

# Generamos el nuevo home2(crud vehiculos)
# Listado de vehiculos
def home2(request):
    
    # Accedemos al objeto que contiene los datos de la base (vehiculos)
    # El metodo all trae todos los vehiculos de la tabla
    vehiculos = Vehiculo.objects.all()

    # La variable datos sera nuestro contexto pasara los datos al template 
    datos = {
        'vehiculos': vehiculos
    }
    return render(request,'core/home2.html',datos)

# Formulario para crear vehiculo
def add_vehiculo(request):
    datos = {
        'form':VehiculoForm()
     }
    if request.method == 'POST':
         formulario_add = VehiculoForm(request.POST)
         if formulario_add.is_valid:
             formulario_add.save()
             datos['mensaje'] = "Vehiculo Agregado Correctamente"
    return render(request, 'core/add_vehiculo.html', datos)

# Formulario para modificar vehiculo
def edit_vehiculo(request, pk):
    vehiculo = Vehiculo.objects.get(patente=pk)
    datos = {
        'form': VehiculoForm(instance=vehiculo)
    }
    if request.method == 'POST':
        formulario_edit = VehiculoForm(data=request.POST, instance=vehiculo)
        if formulario_edit:
            formulario_edit.save()
            datos['mensaje'] = "Los datos han sido modificados"
    return render(request,'core/edit_vehiculo.html', datos)

def delete_vehiculo(request,pk):
    vehiculo = Vehiculo.objects.get(patente=pk)
    vehiculo.delete()
    return redirect(to="home2")        