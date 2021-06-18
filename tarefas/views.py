from rest_framework import generics
from .models import Tarefa
from .serializers import TarefaSerializer


class TarefaLista(generics.ListAPIView):
    queryset = Tarefa.objects.all()
    serializer_class = TarefaSerializer


class TarefaDetalhe(generics.RetrieveAPIView):
    queryset = Tarefa.objects.all()
    serializer_class = TarefaSerializer
