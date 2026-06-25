from django.shortcuts import render

from .models import Livro


def listar_livros(request):
    livros = Livro.objects.select_related("autor").all()

    return render(request, "biblioteca/listar_livros.html", {
        "livros": livros
    })