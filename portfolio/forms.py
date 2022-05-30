from django import forms
from django.forms import ModelForm
from .models import *


class BlogForm(ModelForm):
    class Meta:
        model = Blog
        fields = '__all__'
        # inserção de classes CSS para formatação de cada campo do formulário
        widgets = {
            'autor': forms.TextInput(attrs={'class': 'form-control', 'max': 3, 'min': 1}),
            'data': forms.DateInput(attrs={'class': 'form-control', 'max': 3, 'min': 1}),
            'titulo': forms.TextInput(attrs={'class': 'form-control', 'max': 3, 'min': 1}),
            'descricao': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'descrição da tarefa...'}),
        }

        # texto a exibir junto à janela de inserção
        labels = {
            'autor': 'Autor',
            'data': 'Data',
            'titulo': 'Título',
            'descricao': 'Descrição',
            'imagem': 'Imagem',
        }

        # texto auxiliar a um determinado campo do formulário
        help_texts = {
            'prioridade': 'prioridade: baixa=1, media=2, alta=3',
        }

class DisciplinaForm(ModelForm):
    class Meta:
        model = Disciplina
        fields = '__all__'
        # inserção de classes CSS para formatação de cada campo do formulário
        widgets = {
            'nome': forms.TextInput(attrs={'class': 'form-control', 'max': 3, 'min': 1}),
            'ano': forms.NumberInput(attrs={'class': 'form-control', 'max': 3, 'min': 1}),
            'semestre': forms.NumberInput(attrs={'class': 'form-control', 'max': 2, 'min': 1}),
            'ects': forms.NumberInput(attrs={'class': 'form-control', 'max': 20, 'min': 1}),
        }

        # texto a exibir junto à janela de inserção
        labels = {
            'nome': 'Nome da Disciplina',
            'ano': 'Ano',
            'semestre': 'Semestre',
            'ects': 'ECTS',
        }

class ProjetoForm(ModelForm):
    class Meta:
        model = Projeto
        fields = '__all__'
        # inserção de classes CSS para formatação de cada campo do formulário
        widgets = {
            'titulo': forms.TextInput(attrs={'class': 'form-control'}),
            'descricao': forms.Textarea(attrs={'class': 'form-control'}),
        }

        # texto a exibir junto à janela de inserção
        labels = {
            'titulo': 'Nome do Projeto',
            'image': 'Imagem',
            'descricao': 'Descrição',
        }

