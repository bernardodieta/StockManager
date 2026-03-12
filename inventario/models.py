from django.db import models


class Inventario(models.Model):
	nombre = models.CharField(max_length=150, unique=True)
	descripcion = models.TextField(blank=True)
	creado_en = models.DateTimeField(auto_now_add=True)

	class Meta:
		ordering = ["nombre"]

	def __str__(self):
		return self.nombre


class Categoria(models.Model):
	inventario = models.ForeignKey(
		Inventario,
		on_delete=models.CASCADE,
		related_name="categorias",
	)
	nombre = models.CharField(max_length=120)

	class Meta:
		ordering = ["nombre"]
		constraints = [
			models.UniqueConstraint(
				fields=["inventario", "nombre"],
				name="unique_categoria_por_inventario",
			)
		]

	def __str__(self):
		return f"{self.inventario.nombre} - {self.nombre}"
