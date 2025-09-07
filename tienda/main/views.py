# Importación de la función render para renderizar plantillas
from django.shortcuts import render


# Vista para página de inicio
def inicio(request):
    # Renderizar la plantilla de inicio
    return render(
        request,
        'main/inicio.html'
    )


"""
Explicación (2do commit):
- Se define la función inicio, que renderiza la plantilla de inicio.
- Esta función se puede utilizar para mostrar la página principal de la tienda.
- La plantilla 'main/inicio.html' debe existir en la carpeta de templates
correspondiente.
"""
