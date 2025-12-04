from django.urls import path
from .views import * # el * es para traer todo lo que hay en las views
from django.urls import include


urlpatterns = [
    path("", ListProductView.as_view(),name="lista_productos"),
    path('catalog/', ListProductView.as_view(template_name='Catalog.html'), name='catalog'),
    path('camiseta/<int:pk>/', CamisetaDetailView.as_view(), name='game_detail'),
    path('crear/', CamisetaCreateView.as_view(), name='game_create'),
    path('editar/<int:pk>/', CamisetaUpdateView.as_view(), name='game_update'),
    path('eliminar/<int:pk>/', CamisetaDeleteView.as_view(), name='game_delete'),
    
]