# Importación de la función render para renderizar plantillas
from django.shortcuts import render
# Importación del modelo Producto
from .models import Producto


# Vista para listar productos
def lista_productos(request):
    # Obtener todos los productos con su categoría relacionada
    productos = Producto.objects.all().select_related('categoria')
    """Renderizar la plantilla 'productos/lista_productos.html'
    con el contexto de productos"""
    return render(
        request,
        'productos/lista_productos.html',
        {'productos': productos}
    )


"""
Explicación (1er commit):
- Importamos render y el modelo Producto.
- Definimos la función lista_productos, que obtiene todos los productos
de la base de datos.
- Usamos select_related('categoria') para optimizar la consulta y traer
también la información de la categoría.
- La función retorna el template 'productos/lista_productos.html'
y le pasa la lista de productos.
- Esto permite mostrar todos los productos junto con sus categorías
en la plantilla.s
"""
