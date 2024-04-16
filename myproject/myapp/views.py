from django.shortcuts import render

# Create your views here.
from django.shortcuts import get_object_or_404
from django.http import JsonResponse
from .models import Producto
from django.views.decorators.csrf import csrf_exempt
import json

# Mostrar lista de productos
def mostrar_productos(request):
    productos = Producto.objects.all()
    data = {"productos": list(productos.values())}
    return JsonResponse(data)

# Mostrar los detalles del producto
def mostrar_detalle_producto(request, producto_id):
    producto = get_object_or_404(Producto, id=producto_id)
    data = {"producto": {
        "id": producto.id,
        "nombre": producto.nombre,
        "descripcion": producto.descripcion,
        "precio": str(producto.precio)
    }}
    return JsonResponse(data)

# Añadir producto
@csrf_exempt
def añadir_producto(request):
    if request.method == "POST":
        data = json.loads(request.body)
        producto = Producto.objects.create(
            nombre=data["nombre"],
            descripcion=data["descripcion"],
            precio=data["precio"]
        )
        return JsonResponse({"producto_id": producto.id}, status=201)
    else:
        return JsonResponse({"error": "Método no permitido"}, status=405)

# Borrar producto
@csrf_exempt
def borrar_producto(request, producto_id):
    producto = get_object_or_404(Producto, id=producto_id)
    if request.method == "DELETE":
        producto.delete()
        return JsonResponse({"message": "Producto borrado correctamente"}, status=204)
    else:
        return JsonResponse({"error": "Método no permitido"}, status=405)
