from django import forms
from peliculapp.models import Movies,Genero,Sinopsis
from django.db import models

class pelicula_form(forms.Form):
    titulo = models.CharField(max_length=40)
    duracion = models.FloatField()
    actores = models.CharField(max_length=40)
    año=models.CharField(max_length=4)
    genero=models.CharField(max_length=50)
    description = models.CharField(max_length=200, blank=True, null=True)
    sku = models.CharField(max_length=30, unique=True)
    active = models.BooleanField(default=True)

