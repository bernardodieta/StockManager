from django import forms

from inventario.models import Categoria

from .models import MovimientoStock, ProductoModel, Proveedor


class ProveedorForm(forms.ModelForm):
    class Meta:
        model = Proveedor
        fields = ["nombre", "contacto", "telefono", "email"]

    def clean_nombre(self):
        nombre = self.cleaned_data.get("nombre", "").strip()
        if len(nombre) < 2:
            raise forms.ValidationError("El nombre debe tener al menos 2 caracteres.")
        return nombre


class ProductoForm(forms.ModelForm):
    class Meta:
        model = ProductoModel
        fields = [
            "inventario",
            "categoria",
            "proveedor",
            "nombre",
            "descripcion",
            "stock",
            "imagen",
        ]

    def clean_nombre(self):
        nombre = self.cleaned_data.get("nombre", "").strip()
        if len(nombre) < 3:
            raise forms.ValidationError("El nombre debe tener al menos 3 caracteres.")
        return nombre

    def clean_stock(self):
        stock = self.cleaned_data.get("stock")
        if stock is None:
            return stock
        if stock < 0:
            raise forms.ValidationError("El stock no puede ser negativo.")
        return stock

    def clean(self):
        cleaned_data = super().clean()
        inventario = cleaned_data.get("inventario")
        categoria = cleaned_data.get("categoria")

        if inventario and categoria and categoria.inventario_id != inventario.id:
            self.add_error(
                "categoria",
                "La categoría seleccionada no pertenece al inventario elegido.",
            )
        if not inventario:
            self.add_error("inventario", "Debes seleccionar un inventario.")
        if not categoria:
            self.add_error("categoria", "Debes seleccionar una categoría.")

        return cleaned_data


class MovimientoSalidaForm(forms.ModelForm):
    class Meta:
        model = MovimientoStock
        fields = ["producto", "cantidad", "observacion"]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["producto"].queryset = ProductoModel.objects.select_related(
            "inventario", "categoria"
        )

    def clean_cantidad(self):
        cantidad = self.cleaned_data.get("cantidad")
        if cantidad is None or cantidad <= 0:
            raise forms.ValidationError("La cantidad debe ser mayor a 0.")
        return cantidad

    def clean(self):
        cleaned_data = super().clean()
        producto = cleaned_data.get("producto")
        cantidad = cleaned_data.get("cantidad")

        if producto and cantidad and cantidad > producto.stock:
            self.add_error("cantidad", "No hay stock suficiente para registrar esta salida.")

        return cleaned_data
