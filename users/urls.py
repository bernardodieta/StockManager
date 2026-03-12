from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path

from .views import DashboardView, RegistroView, UserDeleteView, UserListView, UserUpdateView

urlpatterns = [
    path("", DashboardView.as_view(), name="dashboard"),
    path("auth/login/", LoginView.as_view(template_name="users/login.html"), name="login"),
    path("auth/logout/", LogoutView.as_view(next_page="login"), name="logout"),
    path("auth/registro/", RegistroView.as_view(), name="registro"),
    path("usuarios/", UserListView.as_view(), name="users_list"),
    path("usuarios/<int:pk>/editar/", UserUpdateView.as_view(), name="users_update"),
    path("usuarios/<int:pk>/eliminar/", UserDeleteView.as_view(), name="users_delete"),
]
