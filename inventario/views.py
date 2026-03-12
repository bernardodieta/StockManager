from django.urls import reverse_lazy
from django.views.generic import CreateView, DeleteView, ListView, UpdateView

from users.permissions import AdminRequiredMixin

from .forms import CategoriaForm, InventarioForm
from .models import Categoria, Inventario


class InventarioListView(AdminRequiredMixin, ListView):
	model = Inventario
	template_name = "inventario/inventario_list.html"
	context_object_name = "inventarios"


class InventarioCreateView(AdminRequiredMixin, CreateView):
	model = Inventario
	form_class = InventarioForm
	template_name = "inventario/inventario_form.html"
	success_url = reverse_lazy("inventario_list")


class InventarioUpdateView(AdminRequiredMixin, UpdateView):
	model = Inventario
	form_class = InventarioForm
	template_name = "inventario/inventario_form.html"
	success_url = reverse_lazy("inventario_list")


class InventarioDeleteView(AdminRequiredMixin, DeleteView):
	model = Inventario
	template_name = "inventario/inventario_confirm_delete.html"
	success_url = reverse_lazy("inventario_list")


class CategoriaListView(AdminRequiredMixin, ListView):
	model = Categoria
	template_name = "inventario/categoria_list.html"
	context_object_name = "categorias"
	queryset = Categoria.objects.select_related("inventario").all()


class CategoriaCreateView(AdminRequiredMixin, CreateView):
	model = Categoria
	form_class = CategoriaForm
	template_name = "inventario/categoria_form.html"
	success_url = reverse_lazy("categoria_list")


class CategoriaUpdateView(AdminRequiredMixin, UpdateView):
	model = Categoria
	form_class = CategoriaForm
	template_name = "inventario/categoria_form.html"
	success_url = reverse_lazy("categoria_list")


class CategoriaDeleteView(AdminRequiredMixin, DeleteView):
	model = Categoria
	template_name = "inventario/categoria_confirm_delete.html"
	success_url = reverse_lazy("categoria_list")
