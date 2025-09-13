from django.db import models

class Livro(models.Model):
    nome = models.CharField(max_length=100)
    editora = models.CharField(max_length=100)
    publicado = models.DateField()

class Autor(models.Model):
    nome = models.CharField(max_length=100)
    bio = models.CharField(max_length=100)

class Usuario(models.Model):
    nome = models.CharField(max_length=100)
    idade = models.IntegerField(null=True, blank=True)






# Create your models here.
