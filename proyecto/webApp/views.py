
from django.http import HttpResponse
#para renderizar al html
from django.shortcuts import render


from personas.models import Persona
# Create your views here.


def home(request):
   return  HttpResponse("Bienvenido al home")

def bienvenido(request):
    #con objects se accede a la bd
    personas = Persona.objects.all()
    #siempre se le pasa al html es un diccionario 
    return render(request, 'binvenido.html', {'personas': personas})
