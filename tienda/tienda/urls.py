"""
URL configuration for tienda project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
# Importación del módulo admin de Django
from django.contrib import admin
# Importación de path para definir rutas e include para incluir otras URLs
from django.urls import path, include

# Definición de las rutas URL a nivel del proyecto
urlpatterns = [
    path('admin/', admin.site.urls),
    path(
        'productos/',  # Prefijo para las URLs de productos
        include('productos.urls')  # Incluir las URLs de la app productos
    ),
]
