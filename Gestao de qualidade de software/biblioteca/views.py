from django.shortcuts import render, redirect

from .models import Livro, Autor


def listar_livros(request):
    livros = Livro.objects.select_related("autor").all()

    return render(request, "biblioteca/listar_livros.html", {
        "livros": livros
    })

def cadastrar_livro(request):
    if request.method == "POST":
        titulo_recebido = request.POST.get("titulo")
        ano_recebido = request.POST.get("ano")
        autor_id_recebido = request.POST.get("autor")
        
        autor_encontrado = Autor.objects.get(id=autor_id_recebido)
        
        Livro.objects.create(
            titulo=titulo_recebido,
            ano=ano_recebido,
            autor=autor_encontrado,
            disponivel=True
        )
        return redirect("listar_livros")
        
    return render(request, "biblioteca/cadastrar_livro.html")