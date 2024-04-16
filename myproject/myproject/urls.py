"""
URL configuration for myproject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path
from myapp import views

urlpatterns = [
    path('mostrar_productos/', views.mostrar_productos, name='mostrar_productos'),
    path('mostrar_detalle_producto/<int:producto_id>/', views.mostrar_detalle_producto, name='mostrar_detalle_producto'),
    path('añadir_producto/', views.añadir_producto, name='añadir_producto'),
    path('borrar_producto/<int:producto_id>/', views.borrar_producto, name='borrar_producto'),
]