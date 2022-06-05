from django.shortcuts import render

from unicodedata import name
from django.http import HttpResponse

from peliculapp.models import Movies,Genero,Sinopsis
from peliculapp.forms import pelicula_form
from multiprocessing import context


def peliculas(request):
    peliculas = Movies.objects.all()
    context = {'peliculas':peliculas}
    return render(request, 'peliculas.html', context=context)
    print(request.method)
    
def contacto(request):
    return render(request, 'contacto.html')

def crear_pelicula(request):
    if request.method == 'GET':
        form = pelicula_form()
        context = {'form':form}
        return render(request, 'crear_pelicula.html', context=context)
    else:
        form = pelicula_form(request.POST)
        if form.is_valid():
            nueva_pelicula = Movies.objects.create(
                titulo = form.cleaned_data['titulo'],
                duracion = form.cleaned_data['duracion'],
                actores = form.cleaned_data['actores'],
                año = form.cleaned_data['año'],
                genero = form.cleaned_data['genero'],
                descripcion=form.cleaned_data['descripcion'],
                sku = form.cleaned_data['sku'],
                active = form.cleaned_data['active'],
            )
            context ={'nueva_pelicula':nueva_pelicula}
        return render(request, 'crear_pelicula.html', context=context)

def search_pelicula_view(request):
    print(request.GET)
    
    peliculas = Movies.objects.filter(name__contains = request.GET['search'])
    context = {'peliculas':peliculas}
    return render(request, 'search_pelicula.html', context = context)
