from django import forms

from .models import Categoria, Inventario


class InventarioForm(forms.ModelForm):
    class Meta:
        model = Inventario
        fields = ["nombre", "descripcion"]


class CategoriaForm(forms.ModelForm):
    class Meta:
        model = Categoria
        fields = ["inventario", "nombre"]