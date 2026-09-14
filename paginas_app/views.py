from django.shortcuts import render

# Create your views here.
def mostrar_home(request):
    return render(request, 'inicio.html')

def mostrar_acerca(request):
    return render(request, 'acerca-de.html')


def mostrar_servicio(request):
    servicio = {
        "nombre": "Lavado de vehículos",
        "valor": 10000
    }
    return render(request, 'servicio.html', {"servicio": servicio})