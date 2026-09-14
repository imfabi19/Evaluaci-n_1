from django.shortcuts import render

# Create your views here.
def mostrar_home(requests):
    return render(requests, 'inicio.html')

def mostrar_acerca(requests):
    datos: {
        "nombre": "lavado de vehículos",
        "valor": 10000
    }