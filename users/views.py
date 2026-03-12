from django.contrib.auth import login
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.urls import reverse_lazy
from django.views.generic import CreateView, DeleteView, ListView, TemplateView, UpdateView

from inventario.models import Categoria, Inventario
from producto.models import MovimientoStock, ProductoModel

from .forms import RegistroUsuarioForm, UserAdminForm
from .models import UserProfile
from .permissions import AdminRequiredMixin


class DashboardView(LoginRequiredMixin, TemplateView):
	template_name = "dashboard.html"

	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		context["total_productos"] = ProductoModel.objects.count()
		context["total_inventarios"] = Inventario.objects.count()
		context["total_categorias"] = Categoria.objects.count()
		context["ultimos_movimientos"] = MovimientoStock.objects.select_related("producto", "usuario").order_by("-creado_en")[:5]
		return context


class RegistroView(CreateView):
	form_class = RegistroUsuarioForm
	template_name = "users/registro.html"
	success_url = reverse_lazy("dashboard")

	def form_valid(self, form):
		response = super().form_valid(form)
		login(self.request, self.object)
		return response


class UserListView(AdminRequiredMixin, ListView):
	model = User
	template_name = "users/user_list.html"
	context_object_name = "users_list"
	queryset = User.objects.select_related("profile").order_by("username")


class UserUpdateView(AdminRequiredMixin, UpdateView):
	model = User
	form_class = UserAdminForm
	template_name = "users/user_form.html"
	success_url = reverse_lazy("users_list")

	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		context["roles"] = UserProfile.ROLE_CHOICES
		return context


class UserDeleteView(AdminRequiredMixin, DeleteView):
	model = User
	template_name = "users/user_confirm_delete.html"
	success_url = reverse_lazy("users_list")
