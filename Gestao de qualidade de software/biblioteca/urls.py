from django.urls import path

from . import views


urlpatterns = [
    path("livros/", views.listar_livros, name="listar_livros"),
    path("autores/novo/", views.cadastrar_autor, name="cadastrar_autor"),
]