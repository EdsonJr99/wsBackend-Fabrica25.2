from django.contrib import admin
from .models import Livro, Autor, Usuario

admin.site.register(Livro)
admin.site.register(Autor)
admin.site.register(Usuario)

# Register your models here.
