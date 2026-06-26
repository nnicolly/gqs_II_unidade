from django.shortcuts import redirect, render

from .models import Autor, Livro


def listar_livros(request):
    livros = Livro.objects.select_related("autor").all()

    return render(request, "biblioteca/listar_livros.html", {
        "livros": livros
    })


def cadastrar_autor(request):
    if request.method == "POST":
        nome = request.POST.get("nome")
        nacionalidade = request.POST.get("nacionalidade")

        if nome and nacionalidade:
            Autor.objects.create(
                nome=nome,
                nacionalidade=nacionalidade
            )

            return redirect("listar_livros")

    return render(request, "biblioteca/cadastrar_autor.html")