from django.db import models


class Movies(models.Model):
    titulo = models.CharField(max_length=40)
    duracion = models.FloatField()
    actores = models.CharField(max_length=40)
    año=models.CharField(max_length=4)
    sku = models.CharField(max_length=30, unique=True)
    active = models.BooleanField(default=True)

    


class Genero(models.Model):
    genero=models.CharField(max_length=50)
    
  


class Sinopsis(models.Model):
    description = models.CharField(max_length=200, blank=True, null=True)
    
    