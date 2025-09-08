# Importación de serializers de Django REST Framework
from rest_framework import serializers
# Importación de los modelos Producto y Categoria
from .models import Producto, Categoria


# Definición del serializer para el modelo Categoria
class CategoriaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Categoria  # Modelo asociado
        fields = '__all__'  # Incluir todos los campos


# Definición del serializer para el modelo Producto
class ProductoSerializer(serializers.ModelSerializer):
    # Incluir datos de categoría anidados
    categoria = CategoriaSerializer(read_only=True)

    class Meta:
        model = Producto  # Modelo asociado
        fields = '__all__'  # Incluir todos los campos


"""
Explicación:
- Importamos serializers de Django REST Framework para crear serializers.
- Importamos los modelos Producto y Categoria para poder utilizarlos
en los serializers.
- Definimos un serializer para cada modelo, especificando los campos
que queremos incluir.
- En ProductoSerializer, incluimos un campo anidado para la categoría
usando CategoriaSerializer.
- Esto permite convertir instancias de los modelos a formatos como
JSON para APIs.
"""
