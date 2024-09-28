from django.shortcuts import get_object_or_404, render
from .models import Producto, Categoria

def index(request):
    product_list = Producto.objects.order_by('nombre')[:6] 
    context = {'product_list': product_list}
    return render(request, 'index.html', context)

def producto(request, producto_id):
    producto = get_object_or_404(Producto, pk=producto_id)  
    return render(request, 'producto.html', {'producto': producto})

def categoria_productos(request, categoria_id):
    categoria = get_object_or_404(Categoria, pk=categoria_id) 
    productos = Producto.objects.filter(categoria=categoria)  
    return render(request, 'categoria_productos.html', {'categoria': categoria, 'productos': productos})