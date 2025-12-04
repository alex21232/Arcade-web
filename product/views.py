from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Juego  # Cambiamos Camiseta por Juego

class ListProductView(ListView):
    model = Juego
    template_name = "home.html"
    context_object_name = "juegos"  # Cambiado a "juegos"

class JuegoDetailView(DetailView):  # Cambiado nombre de clase
    model = Juego
    template_name = 'detail_product.html'
    context_object_name = 'juego'  # Cambiado a "juego"

# DELETE VIEW - Eliminar juego
class JuegoDeleteView(DeleteView):  # Cambiado nombre de clase
    model = Juego
    template_name = 'delete_product.html'
    success_url = reverse_lazy("lista_productos")
    success_message = "¡Juego eliminado exitosamente!"  # Cambiado mensaje

# UPDATE VIEW - Editar juego existente
class JuegoUpdateView(UpdateView):  # Cambiado nombre de clase
    model = Juego
    template_name = 'update_product.html'
    success_url = reverse_lazy("lista_productos")
    success_message = "¡Juego actualizado exitosamente!"  # Cambiado mensaje
    fields = [
        'nombre',
        'plataforma',  # Cambiado 'equipo' por 'plataforma'
        'genero',      # Cambiado 'temporada' por 'genero'
        'desarrollador', # Podría ser similar a 'talla'
        'descripcion',
        'precio',
        'imagen',
        'publicado',
        'vendido'
    ]

# CREATE VIEW - Crear nuevo juego
class JuegoCreateView(CreateView):  # Cambiado nombre de clase
    model = Juego
    template_name = 'create_product.html'
    success_url = reverse_lazy("lista_productos")
    success_message = "¡Juego creado exitosamente!"  # Cambiado mensaje
    fields = [
        'nombre',
        'plataforma',   # Cambiado 'equipo' por 'plataforma'
        'genero',       # Cambiado 'temporada' por 'genero'
        'desarrollador', # Podría ser similar a 'talla'
        'descripcion',
        'precio',
        'imagen',
        'publicado'
    ]