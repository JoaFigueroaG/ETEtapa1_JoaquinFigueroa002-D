from django.urls import path
from . import views

urlpatterns = [
    path('', views.hub, name = "hub"),
    path('index/', views.index, name = "index"),
    path('subir/', views.subir, name = "subir"),
    path('editar/<int:proveedores_id>/', views.editar, name = "editar"),
    path('eliminar/<int:proveedores_id>/', views.eliminar, name = "eliminar"),
]
