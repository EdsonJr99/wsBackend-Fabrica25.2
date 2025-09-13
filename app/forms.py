from django import forms
from .models import Livro, Autor, Usuario


class LivroForm(forms.ModelForm):
    class Meta:
        model = Livro
        fields = ["nome", "editora", "publicado"]

class AutorForm(forms.ModelForm):
    class Meta:
        model = Autor
        fields = ["nome", "bio"]

class UsuarioForm(forms.ModelForm):
    class Meta:
        model = Usuario
        fields = ["nome", "idade"]