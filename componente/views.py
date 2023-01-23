from django.shortcuts import render, redirect
from componente.forms import ComponenteForm
from componente.models import Componente
from .models import Ingredientes

# Create your views here.
def componente(request):
    titulo='Componente'
    componente=Componente.objects.all()
    context={
        'titulo':titulo,
        'componente':componente
    }
    return render(request,'componente/componente.html',context)

def ingredientes(request):
    ingredientes = Ingredientes.objects.all()
    print(ingredientes)
    return render(request,'ingrediente/ingrediente.html')