from django.contrib import admin

from .models import Categoria, Inventario


@admin.register(Inventario)
class InventarioAdmin(admin.ModelAdmin):
	list_display = ("id", "nombre", "creado_en")
	search_fields = ("nombre",)


@admin.register(Categoria)
class CategoriaAdmin(admin.ModelAdmin):
	list_display = ("id", "nombre", "inventario")
	list_filter = ("inventario",)
	search_fields = ("nombre", "inventario__nombre")
