from django.db import models

class Livro(models.Model):
    titulo = models.CharField(max_length=100)
    editora = models.CharField(max_length=100)
    publicado = models.DateField()

    def __str__(self):
        return self.titulo

class Autor(models.Model):
    nome_autor = models.CharField(max_length=100)
    bio = models.CharField(max_length=100)

    def __str__(self):
        return self.nome_autor

class Usuario(models.Model):
    nome_usuario = models.CharField(max_length=100)
    idade = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return self.nome_usuario






# Create your models here.
