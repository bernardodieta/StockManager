from django.db import models
from django.contrib.auth.models import User

from inventario.models import Categoria, Inventario


class Proveedor(models.Model):
    nombre = models.CharField(max_length=250, unique=True)
    contacto = models.CharField(max_length=250, blank=True)
    telefono = models.CharField(max_length=50, blank=True)
    email = models.EmailField(blank=True)

    class Meta:
        ordering = ["nombre"]

    def __str__(self):
        return self.nombre


class ProductoModel(models.Model):
    inventario = models.ForeignKey(
        Inventario,
        on_delete=models.PROTECT,
        related_name="productos",
        null=True,
        blank=True,
    )
    categoria = models.ForeignKey(
        Categoria,
        on_delete=models.PROTECT,
        related_name="productos",
        null=True,
        blank=True,
    )
    proveedor = models.ForeignKey(
        Proveedor,
        on_delete=models.SET_NULL,
        related_name="productos",
        null=True,
        blank=True,
    )
    nombre = models.CharField(max_length=250, unique=True)
    descripcion = models.TextField(null=True, blank=True)
    stock = models.IntegerField(null=False)
    Fecha_ingreso = models.DateField(auto_now_add=True)
    imagen = models.ImageField(upload_to="media/")

    def __str__(self):
        inventario_nombre = self.inventario.nombre if self.inventario else "Sin inventario"
        categoria_nombre = self.categoria.nombre if self.categoria else "Sin categoría"
        return f"{self.nombre} ({inventario_nombre} - {categoria_nombre})"

    def __str__(self):
        inventario_nombre = self.inventario.nombre if self.inventario else "Sin inventario"
        categoria_nombre = self.categoria.nombre if self.categoria else "Sin categoría"
        return f"{self.nombre} ({inventario_nombre} - {categoria_nombre})"


class MovimientoStock(models.Model):
    TIPO_ENTRADA = "entrada"
    TIPO_SALIDA = "salida"
    TIPO_CHOICES = [
        (TIPO_ENTRADA, "Entrada"),
        (TIPO_SALIDA, "Salida"),
    ]

    producto = models.ForeignKey(
        ProductoModel,
        on_delete=models.CASCADE,
        related_name="movimientos",
    )
    tipo = models.CharField(max_length=10, choices=TIPO_CHOICES, default=TIPO_SALIDA)
    cantidad = models.PositiveIntegerField()
    observacion = models.CharField(max_length=255, blank=True)
    usuario = models.ForeignKey(User, on_delete=models.PROTECT, related_name="movimientos")
    creado_en = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-creado_en"]

    def __str__(self):
        return f"{self.producto.nombre} - {self.tipo} - {self.cantidad}"
