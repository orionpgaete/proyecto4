from django.shortcuts import render
from django.http import HttpResponse
from gestionPedidos.models import Articulos

# Create your views here.


#python -m django startproject proyecto4  #crear proyecto
#cd proyecto4 # abrir carpeta
#python manage.py startapp gestionPedidos # crear APP

def busqueda(request):
    return render(request, "busqueda.html")

def buscar(request):
    if request.GET["prd"]:
        #mensaje = "Articulo buscado: %r" %request.GET["prd"]
        producto = request.GET["prd"]
        prod = Articulos.objects.filter(nombre__icontains=producto)
        return render(request, "resultado.html", {"articulos":prod, "query":producto} )
    else:
        mensaje = "No has introducido nada de nada"
    return HttpResponse(mensaje)