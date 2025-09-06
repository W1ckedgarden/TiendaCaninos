# Importación de models de django.db
from django.db import models


# Modelo para Categorías de Productos
class Categoria(models.Model):
    # Nombre de la categoría (único)
    nombre = models.CharField(
        max_length=100,  # Longitud máxima de 100 caracteres
        unique=True,  # Nombre único
        verbose_name="Nombre"  # Nombre legible
    )
    # Descripción de la categoría (opcional)
    descripcion = models.TextField(
        blank=True,  # Campo opcional
        null=True,  # Permitir nulos
        verbose_name="Descripción"  # Nombre legible
    )
    # Fecha de creación automática
    fecha_creacion = models.DateTimeField(
        auto_now_add=True,  # Fecha de creación automática
        verbose_name="Fecha de Creación"  # Nombre legible
    )

    # Configuración del modelo
    class Meta:
        verbose_name = "Categoría"  # Nombre singular
        verbose_name_plural = "Categorías"  # Nombre plural
        ordering = ['nombre']  # Ordenar alfabéticamente

    # Representación en texto
    def __str__(self):
        return self.nombre  # Mostrar el nombre de la categoría


# Modelo para Productos
class Producto(models.Model):
    # Categoría del producto (relación con Categoría)
    # ForeignKey: Relación "muchos a uno" (muchos productos -> una categoría)
    categoria = models.ForeignKey(
        Categoria,
        on_delete=models.PROTECT,  # Proteger la categoría de eliminación
        verbose_name="Categoría"  # Nombre legible
    )
    # Nombre del producto (obligatorio)
    nombre = models.CharField(
        max_length=200,  # Longitud máxima de 200 caracteres
        verbose_name="Nombre"  # Nombre legible
    )
    # Descripción detallada (opcional)
    descripcion = models.TextField(
        blank=True,  # Campo opcional
        verbose_name="Descripción"  # Nombre legible
    )
    # Precio del producto (obligatorio, con 2 decimales)
    precio = models.DecimalField(
        max_digits=10,  # Máximo de 10 dígitos
        decimal_places=2,  # 2 decimales
        verbose_name="Precio"  # Nombre legible
    )
    # Stock actual en bodega (obligatorio)
    stock = models.PositiveIntegerField(
        default=0,  # Stock inicial
        verbose_name="Stock"  # Nombre legible
    )
    # Stock mínimo recomendado
    stock_minimo = models.PositiveIntegerField(
        default=5,  # Stock mínimo recomendado
        verbose_name="Stock Mínimo"  # Nombre legible
    )
    # Fecha de creación automatica
    fecha_creacion = models.DateTimeField(
        auto_now_add=True,  # Fecha de creación automática
        verbose_name="Fecha de Creación"  # Nombre legible
    )

    # Configuracion del modelo Producto
    class Meta:
        verbose_name = "Producto"  # Nombre singular
        verbose_name_plural = "Productos"  # Nombre plural
        ordering = ['id']  # Ordenar por id

    # Representación en cadena de texto del modelo Producto
    def __str__(self):
        return f"{self.id} - {self.nombre}"  # Mostrar id y nombre del producto


"""
Explicación:
- El modelo Categoria representa las categorías de productos en la tienda.
- Tiene campos para el nombre, descripción y fecha de creación.
- El modelo Producto representa los productos en la tienda.
- Tiene campos para la categoría, nombre, descripción, precio, stock,
stock mínimo y fecha de creación.
- Ambos modelos tienen una representación en cadena de texto que muestra
información relevante.
- La clase Meta en ambos modelos define configuraciones adicionales como
nombres legibles y ordenamiento predeterminado.
"""
