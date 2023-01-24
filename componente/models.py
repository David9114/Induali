from django.db import models
from django.utils.translation import gettext_lazy as _


class Componente (models.Model):
   codComponente=models.TextField(max_length=50, verbose_name="Código Componente")
   nomComponente=models.TextField(max_length=50, verbose_name="Nombre Componente")

# class Ingredientes (models.Model):
#       idIngrediente = models.AutoField(primary_key=True)
#       nameIngrediente = models.CharField(max_length=100, verbose_name='Nombre')
#       unidad = models.CharField(max_length=100, verbose_name='UnidadMedida')
#       cantMP = models.IntegerField()
#       stateRow = models.CharField(max_length=1, verbose_name='EstadoFila', default='A')
      
#       def __str__(self):
#          fila = "Nombre: "+ self.nameIngrediente + " - Unidad: " + self.unidad 
#          return fila