from django.urls import path

from peliculapp.views import peliculas, contacto, crear_pelicula, search_pelicula_view

urlpatterns = [
    path('', peliculas, name = 'peliculas'),
    path('contacto/', contacto, name = 'contacto'),
    path('create-pelicula/', crear_pelicula, name = 'create-pelicula'),
    path('search-pelicula/', search_pelicula_view, name = 'search_pelicula_view'),
]