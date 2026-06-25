from django.urls import path

from . import views


urlpatterns = [
    path("livros/", views.listar_livros, name="listar_livros"),
    path("livros/cadastrar/", views.cadastrar_livro, name="cadastrar_livro"),
]