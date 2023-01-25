# Generated by Django 4.1.5 on 2023-01-25 13:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ingrediente', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ingrediente',
            name='codIngrediente',
            field=models.CharField(max_length=50, verbose_name='Codigo Ingrediente'),
        ),
        migrations.AlterField(
            model_name='ingrediente',
            name='nomIngrediente',
            field=models.CharField(max_length=50, verbose_name='Nombre Ingrediente'),
        ),
        migrations.AlterField(
            model_name='ingrediente',
            name='unidadMedida',
            field=models.CharField(max_length=50, verbose_name='Unidad de Medida'),
        ),
    ]