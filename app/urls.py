from django.urls import path
from .views import LivroListView, LivroCreateView, LivroUpdateView, LivroDeleteView, AutorListView, AutorCreateView, AutorUpdateView, AutorDeleteView, UsuarioListView, UsuarioCreateView, UsuarioUpdateView, UsuarioDeleteView
from . import views
from rest_framework_simplejwt.views import (TokenObtainPairView, TokenRefreshView)

urlpatterns = [path("", views.home, name="home"),
               path('api/token', TokenObtainPairView.as_view(), name="token_obtain_pair"),
               path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
               path("buscar/", views.buscar_livros, name="buscar_livros"),
               path("listar", LivroListView.as_view(), name="listar_livros"),
               path("adicionar", LivroCreateView.as_view(), name="adicionar_livro"),
               path("atualizar/<int:pk>", LivroUpdateView.as_view(), name="atualizar_livro"),
               path("deletar/<int:pk>", LivroDeleteView.as_view(), name="deletar_livro"),
               path("listarAut", AutorListView.as_view(), name="listar_autores"),
               path("adicionarAut", AutorCreateView.as_view(), name="adicionar_autor"),
               path("atualizarAut/<int:pk>", AutorUpdateView.as_view(), name="atualizar_autor"),
               path("deletarAut/<int:pk>", AutorDeleteView.as_view(), name="deletar_autor"),
               path("listarUsu", UsuarioListView.as_view(), name="listar_usuarios"),
               path("adicionarUsu", UsuarioCreateView.as_view(), name="adicionar_usuario"),
               path("atualizarUsu/<int:pk>", UsuarioUpdateView.as_view(), name="atualizar_usuario"),
               path("deletarUsu/<int:pk>", UsuarioDeleteView.as_view(), name="deletar_usuario"),
]