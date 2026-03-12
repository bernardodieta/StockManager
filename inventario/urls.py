from django.urls import path

from .views import (
    CategoriaCreateView,
    CategoriaDeleteView,
    CategoriaListView,
    CategoriaUpdateView,
    InventarioCreateView,
    InventarioDeleteView,
    InventarioListView,
    InventarioUpdateView,
)

urlpatterns = [
    path("", InventarioListView.as_view(), name="inventario_list"),
    path("nuevo/", InventarioCreateView.as_view(), name="inventario_create"),
    path("<int:pk>/editar/", InventarioUpdateView.as_view(), name="inventario_update"),
    path("<int:pk>/eliminar/", InventarioDeleteView.as_view(), name="inventario_delete"),
    path("categorias/", CategoriaListView.as_view(), name="categoria_list"),
    path("categorias/nuevo/", CategoriaCreateView.as_view(), name="categoria_create"),
    path("categorias/<int:pk>/editar/", CategoriaUpdateView.as_view(), name="categoria_update"),
    path("categorias/<int:pk>/eliminar/", CategoriaDeleteView.as_view(), name="categoria_delete"),
]
