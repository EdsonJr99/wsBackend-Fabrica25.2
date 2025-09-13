from django.shortcuts import render
from .models import Livro, Autor, Usuario
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from .forms import LivroForm
from django.urls import reverse_lazy
from django.views import View
from django.http import HttpResponse


class HelloView(View):
    def get(self, request):
        return HttpResponse('lesgo')
    

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






# Create your views here.
