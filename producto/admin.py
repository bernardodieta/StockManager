from django.contrib import admin

from .models import MovimientoStock, ProductoModel, Proveedor


@admin.register(Proveedor)
class ProveedorAdmin(admin.ModelAdmin):
	list_display = ("id", "nombre", "contacto", "telefono", "email")
	search_fields = ("nombre", "contacto", "email")


@admin.register(ProductoModel)
class ProductoModelAdmin(admin.ModelAdmin):
	list_display = (
		"id",
		"nombre",
		"inventario",
		"categoria",
		"stock",
		"proveedor",
		"Fecha_ingreso",
	)
	list_filter = ("inventario", "categoria", "proveedor")
	search_fields = ("nombre", "proveedor__nombre", "inventario__nombre", "categoria__nombre")


@admin.register(MovimientoStock)
class MovimientoStockAdmin(admin.ModelAdmin):
	list_display = ("id", "producto", "tipo", "cantidad", "usuario", "creado_en")
	list_filter = ("tipo", "producto__inventario")
	search_fields = ("producto__nombre", "usuario__username")
