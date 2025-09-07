# Importación de path para definir rutas
from django.urls import path
# Importación de las vistas del módulo main
from . import views

# Definición de las rutas URL para la aplicación principal
urlpatterns = [
    path(
        '',  # URL raíz de la app main
        views.inicio,  # Vista asociada
        name='inicio'  # Nombre de la ruta
    ),
]

"""
Explicación (2do commit):
- Se define la ruta para la página de inicio de la aplicación principal.
- La vista asociada es 'inicio', que renderiza la plantilla 'main/inicio.html'.
- Esta ruta se puede utilizar para mostrar la página principal de la tienda.
- El nombre 'inicio' facilita la referencia a esta ruta en otras
partes del proyecto.
"""
