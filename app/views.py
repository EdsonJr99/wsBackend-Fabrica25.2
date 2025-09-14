from django.shortcuts import render
from .models import Livro, Autor, Usuario
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from .forms import LivroForm, AutorForm, UsuarioForm
from django.urls import reverse_lazy
from django.views import View
from django.http import HttpResponse
from .services import buscar_livros_google
import requests



def home(request):
    return render(request, 'home.html')
    
def buscar_livros(request):
    query = request.GET.get("q")
    resultados = []

    if query:
        resultados = buscar_livros_google(query)

    return render(request, "buscarlivro.html", {
        "resultados": resultados,
        "query": query
    })

class LivroListView(ListView):
    model = Livro
    template_name = "list.html"
    context_object_name = "livros"

class LivroCreateView(CreateView):
    model = Livro
    form_class = LivroForm
    template_name = "adicionarlivro.html"
    success_url = reverse_lazy("listar_livros")

class LivroUpdateView(UpdateView):
    model = Livro
    form_class = LivroForm
    template_name = "adicionarlivro.html"
    context_object_name = ("livro")
    success_url = reverse_lazy("listar_livros")

class LivroDeleteView(DeleteView):
    model = Livro
    template_name = "deletarlivro.html"
    context_object_name = ("livro")
    success_url = reverse_lazy("listar_livros")


class AutorListView(ListView):
    model = Autor
    template_name = "list_autor.html"
    context_object_name = "autores"

class AutorCreateView(CreateView):
    model = Autor
    form_class = AutorForm
    template_name = "adicionarautor.html"
    success_url = reverse_lazy("listar_autores")

class AutorUpdateView(UpdateView):
    model = Autor
    form_class = AutorForm
    template_name = "adicionarautor.html"
    context_object_name = ("autor")
    success_url = reverse_lazy("listar_autores")

class AutorDeleteView(DeleteView):
    model = Autor
    template_name = "deletarautor.html"
    context_object_name = ("autor")
    success_url = reverse_lazy("listar_autores")


class UsuarioListView(ListView):
    model = Usuario
    template_name = "list_usuario.html"
    context_object_name = "usuarios"

class UsuarioCreateView(CreateView):
    model = Usuario
    form_class = UsuarioForm
    template_name = "adicionarusuario.html"
    success_url = reverse_lazy("listar_usuarios")

class UsuarioUpdateView(UpdateView):
    model = Usuario
    form_class = UsuarioForm
    template_name = "adicionarusuario.html"
    context_object_name = ("usuario")
    success_url = reverse_lazy("listar_usuarios")

class UsuarioDeleteView(DeleteView):
    model = Usuario
    template_name = "deletarusuario.html"
    context_object_name = ("usuario")
    success_url = reverse_lazy("listar_usuarios")







# Create your views here.
