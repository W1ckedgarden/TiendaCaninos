# Importación de path para definir rutas
from django.urls import path
# Importación de las vistas del módulo actual
from . import views

# Definición de las rutas URL para la aplicación de productos
urlpatterns = [
    path(
        'lista/',  # URL para listar productos
        views.lista_productos,  # Vista asociada
        name='lista_productos'  # Nombre de la ruta
    ),
]

"""
Explicación:
- Importamos path de django.urls para definir rutas URL.
- Importamos las vistas del módulo actual (views).
- Definimos una lista urlpatterns que contiene las rutas URL.
- La ruta 'lista/' está asociada a la vista lista_productos.
- Asignamos el nombre 'lista_productos' a esta ruta para facilitar su
referencia en otras partes del proyecto.
"""
