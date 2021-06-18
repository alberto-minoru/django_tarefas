from django.test import TestCase
from .models import Tarefa


class TarefaModelTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        Tarefa.objects.create(titulo='tarefa teste', descricao='descrição teste')

    def test_conteudo_titulo(self):
        tarefa = Tarefa.objects.get(id=1)
        conteudo = f'{tarefa.titulo}'
        self.assertEqual(conteudo, 'tarefa teste')

    def test_conteudo_descricao(self):
        tarefa = Tarefa.objects.get(id=1)
        conteudo = f'{tarefa.descricao}'
        self.assertEqual(conteudo, 'descrição teste')
