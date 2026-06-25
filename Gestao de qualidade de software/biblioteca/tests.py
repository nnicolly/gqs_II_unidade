from django.test import TestCase
from django.urls import reverse

from .models import Autor, Livro


class TestesBiblioteca(TestCase):

    def setUp(self):
        self.autor = Autor.objects.create(
            nome="Machado de Assis",
            nacionalidade="Brasileira"
        )

        Livro.objects.create(
            titulo="Dom Casmurro",
            ano=1899,
            disponivel=True,
            autor=self.autor
        )

        Livro.objects.create(
            titulo="Memórias Póstumas de Brás Cubas",
            ano=1881,
            disponivel=False,
            autor=self.autor
        )

    def test_listagem_de_livros_exibe_livros_cadastrados(self):
        response = self.client.get(reverse("listar_livros"))

        self.assertEqual(response.status_code, 200)

        self.assertContains(response, "Dom Casmurro")
        self.assertContains(response, "Memórias Póstumas de Brás Cubas")
        self.assertContains(response, "1899")
        self.assertContains(response, "1881")
        self.assertContains(response, "Machado de Assis")
        self.assertContains(response, "Disponível")
        self.assertContains(response, "Emprestado")

        self.assertTemplateUsed(response, "biblioteca/listar_livros.html")


    def test_cadastrar_livro(self):
        dados_formulario = {
            "titulo": "O Alienista",
            "ano": 1882,
            "autor": self.autor.id 
        }

        resposta = self.client.post(reverse("cadastrar_livro"), dados_formulario)

        self.assertEqual(resposta.status_code, 302)

        quantidade_livros = Livro.objects.count()
        self.assertEqual(quantidade_livros, 3)

        livro_salvo = Livro.objects.last()
        self.assertEqual(livro_salvo.titulo, "O Alienista")
        self.assertEqual(livro_salvo.autor, self.autor)