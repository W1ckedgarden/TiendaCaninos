# Importación el módulo admin de Django
from django.contrib import admin
# Importación de los modelos Categoria y Producto
from .models import Categoria, Producto

# Modelos registrados en el admin de Django
admin.site.register(Categoria)
admin.site.register(Producto)

"""
Explicación:
- Importamos admin de django.contrib para registrar nuestros
modelos en el admin.
- Importamos los modelos Categoria y Producto del módulo actual (models).
- Registramos los modelos en el sitio admin de Django para que sean accesibles
desde la interfaz de administración.
"""
