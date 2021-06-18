from django.urls import path
from .views import TarefaLista, TarefaDetalhe

urlpatterns = [
    path('<int:pk>/', TarefaDetalhe.as_view()),
    path('', TarefaLista.as_view()),
]
