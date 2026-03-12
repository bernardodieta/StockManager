from django.urls import path

from .views import (
    MovimientoSalidaCreateView,
    MovimientoSalidaListView,
    ProductoCreateView,
    ProductoDetailView,
    ProductoDeleteView,
    ProductoListView,
    ProductoUpdateView,
    ProveedorCreateView,
    ProveedorDeleteView,
    ProveedorListView,
    ProveedorQuickCreateView,
    ProveedorUpdateView,
)

urlpatterns = [
    path("", ProductoListView.as_view(), name="producto_list"),
    path("<int:pk>/", ProductoDetailView.as_view(), name="producto_detail"),
    path("nuevo/", ProductoCreateView.as_view(), name="producto_create"),
    path("<int:pk>/editar/", ProductoUpdateView.as_view(), name="producto_update"),
    path("<int:pk>/eliminar/", ProductoDeleteView.as_view(), name="producto_delete"),
    path("salida/", MovimientoSalidaCreateView.as_view(), name="movimiento_salida"),
    path("salidas/", MovimientoSalidaListView.as_view(), name="movimiento_salida_list"),
    path("proveedores/", ProveedorListView.as_view(), name="proveedor_list"),
    path("proveedores/nuevo/", ProveedorCreateView.as_view(), name="proveedor_create"),
    path("proveedores/<int:pk>/editar/", ProveedorUpdateView.as_view(), name="proveedor_update"),
    path("proveedores/<int:pk>/eliminar/", ProveedorDeleteView.as_view(), name="proveedor_delete"),
    path("proveedores/rapido/", ProveedorQuickCreateView.as_view(), name="proveedor_quick_create"),
]
