from django.contrib import messages
from django.db import transaction
from django.http import HttpResponseRedirect, JsonResponse
from django.urls import reverse_lazy
from django.views.generic import CreateView, DeleteView, DetailView, ListView, UpdateView

from users.permissions import AdminRequiredMixin, EmployeeOrAdminRequiredMixin

from .forms import MovimientoSalidaForm, ProductoForm, ProveedorForm
from .models import MovimientoStock, ProductoModel, Proveedor


class ProveedorListView(AdminRequiredMixin, ListView):
	model = Proveedor
	template_name = "producto/proveedor_list.html"
	context_object_name = "proveedores"


class ProveedorCreateView(AdminRequiredMixin, CreateView):
	model = Proveedor
	template_name = "producto/proveedor_form.html"
	form_class = ProveedorForm
	success_url = reverse_lazy("proveedor_list")


class ProveedorUpdateView(AdminRequiredMixin, UpdateView):
	model = Proveedor
	template_name = "producto/proveedor_form.html"
	form_class = ProveedorForm
	success_url = reverse_lazy("proveedor_list")


class ProveedorDeleteView(AdminRequiredMixin, DeleteView):
	model = Proveedor
	template_name = "producto/proveedor_confirm_delete.html"
	success_url = reverse_lazy("proveedor_list")


class ProveedorQuickCreateView(AdminRequiredMixin, CreateView):
	model = Proveedor
	form_class = ProveedorForm

	def form_valid(self, form):
		proveedor = form.save()
		return JsonResponse({"id": proveedor.pk, "nombre": proveedor.nombre})

	def form_invalid(self, form):
		errors = {field: e.get_json_data() for field, e in form.errors.items()}
		return JsonResponse({"errors": errors}, status=400)


class ProductoListView(EmployeeOrAdminRequiredMixin, ListView):
	model = ProductoModel
	template_name = "producto/producto_list.html"
	context_object_name = "productos"
	queryset = ProductoModel.objects.select_related("inventario", "categoria", "proveedor")


class ProductoCreateView(AdminRequiredMixin, CreateView):
	model = ProductoModel
	template_name = "producto/producto_form.html"
	form_class = ProductoForm
	success_url = reverse_lazy("producto_list")


class ProductoUpdateView(AdminRequiredMixin, UpdateView):
	model = ProductoModel
	template_name = "producto/producto_form.html"
	form_class = ProductoForm
	success_url = reverse_lazy("producto_list")


class ProductoDeleteView(AdminRequiredMixin, DeleteView):
	model = ProductoModel
	template_name = "producto/producto_confirm_delete.html"
	success_url = reverse_lazy("producto_list")


class MovimientoSalidaCreateView(EmployeeOrAdminRequiredMixin, CreateView):
	model = MovimientoStock
	template_name = "producto/movimiento_form.html"
	form_class = MovimientoSalidaForm
	success_url = reverse_lazy("producto_list")

	def form_valid(self, form):
		with transaction.atomic():
			movimiento = form.save(commit=False)
			movimiento.tipo = MovimientoStock.TIPO_SALIDA
			movimiento.usuario = self.request.user
			producto = movimiento.producto
			producto.stock -= movimiento.cantidad
			producto.save(update_fields=["stock"])
			movimiento.save()
			self.object = movimiento
		messages.success(self.request, "Salida de stock registrada correctamente.")
		return HttpResponseRedirect(self.get_success_url())


class MovimientoSalidaListView(AdminRequiredMixin, ListView):
	model = MovimientoStock
	template_name = "producto/movimiento_list.html"
	context_object_name = "movimientos"
	queryset = MovimientoStock.objects.select_related(
		"producto",
		"producto__inventario",
		"producto__categoria",
		"usuario",
	).filter(tipo=MovimientoStock.TIPO_SALIDA)


class ProductoDetailView(EmployeeOrAdminRequiredMixin, DetailView):
	model = ProductoModel
	template_name = "producto/producto_detail.html"
	context_object_name = "producto"
	queryset = ProductoModel.objects.select_related("inventario", "categoria", "proveedor")
