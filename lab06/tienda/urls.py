from django.urls import path
from . import views

app_name = 'tienda'

urlpatterns = [
    path('', views.index, name='index'),  # Página principal que muestra productos
    path('producto/<int:producto_id>/', views.producto, name='producto'),  # Vista de un producto específico
    path('categoria/<int:categoria_id>/', views.categoria_productos, name='categoria'),  # Vista de productos por categoría
]