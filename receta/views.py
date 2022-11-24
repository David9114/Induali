from django.shortcuts import render, redirect
from receta.models import Receta
from receta.forms import RecetaForm

# Create your views here.
def receta(request):
    titulo='Receta'
    receta=Receta.objects.all()
    context={
        'titulo':titulo,
        'receta':receta
    }
    return render(request,'receta/receta.html',context)