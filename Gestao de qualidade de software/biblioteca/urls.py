from django.urls import path

from . import views


urlpatterns = [
    path("livros/", views.listar_livros, name="listar_livros"),
    path("autores/novo/", views.cadastrar_autor, name="cadastrar_autor"),
    path("livros/cadastrar/", views.cadastrar_livro, name="cadastrar_livro"),
    path("livros/<int:livro_id>/emprestar/", views.emprestar_livro, name="emprestar_livro"),
]