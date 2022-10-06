from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


#python -m django startproject proyecto4  #crear proyecto
#cd proyecto4 # abrir carpeta
#python manage.py startapp gestionPedidos # crear APP

def busqueda(request):
    return render(request, "busqueda.html")

def buscar(request):
    mensaje = "Articulo buscado: %r" %request.GET["prd"]
    return HttpResponse(mensaje)