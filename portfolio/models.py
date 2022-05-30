from django.db import models

# Create your models here.

from django.db import models


class Blog(models.Model):
    autor = models.CharField(max_length=30, null=True)
    data = models.DateField()
    titulo = models.CharField(max_length=30, null=True)
    descricao = models.TextField()
    imagem = models.ImageField(upload_to='images/', blank=True, null=True)


class PontuacaoQuizz(models.Model):
    nome = models.CharField(max_length=30, null=True)
    pontos = models.IntegerField()


class Disciplina(models.Model):
    nome = models.CharField(max_length=30, null=True)
    ano = models.IntegerField()
    semestre = models.IntegerField()
    ects = models.IntegerField()


class Projeto(models.Model):
    titulo = models.CharField(max_length=30, null=True)
    image = models.ImageField(blank=True, null=True)
    descricao = models.TextField()
