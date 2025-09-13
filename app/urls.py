from django.urls import path
from .views import HelloView, LivroListView, LivroCreateView, LivroUpdateView, LivroDeleteView

urlpatterns = [path("", HelloView.as_view(), name="index"),
               path("listar", LivroListView.as_view(), name="listar_livros"),
               path("adicionar", LivroCreateView.as_view(), name="adicionar_livro"),
               path("atualizar/<int:pk>", LivroUpdateView.as_view(), name="atualizar_livro"),
               path("deletar/<int:pk>", LivroDeleteView.as_view(), name="deletar_livro"),
]