# Se crea archivo python para guardar urls 
# Por cada aplicacion que se cree en django se crea un url
from django.urls import path
from .views import home, blog, blog2, home2, add_vehiculo, edit_vehiculo, delete_vehiculo

urlpatterns =[ 
    path('', home, name="home"),
    path('home2/',home2, name="home2"),
    path('agregar-vehiculo/', add_vehiculo, name="add_vehiculo"),
    path('editar-vehiculo/<pk>',edit_vehiculo, name="edit_vehiculo"),
    path('eliminar-vehiculo/<pk>',delete_vehiculo, name="delete_vehiculo"),
    path('blog/', blog, name="blog"),
    path('blog2/',blog2, name="blog2"),
] 