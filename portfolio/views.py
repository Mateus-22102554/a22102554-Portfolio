from django.http import HttpResponseRedirect
from django.shortcuts import render
import datetime
from matplotlib import pyplot as plt
from django.urls import reverse

from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth.decorators import login_required

from .forms import *
from .models import *


# Create your views here.

def capa_page_view(request):
    return render(request, 'portfolio/capa.html')


def home_page_view(request):
    agora = datetime.datetime.now()
    local = 'Lisboa'

    context = {
        'hora': agora.hour,
        'local': local,

    }

    return render(request, 'portfolio/home.html', context)


def layout_page_view(request):
    return render(request, 'portfolio/layout.html')


def apresentacao_page_view(request):
    return render(request, 'portfolio/apresentacao.html')


def competencias_page_view(request):
    return render(request, 'portfolio/competencias.html')


def formacao_page_view(request):
    return render(request, 'portfolio/formacao.html')


def blog_page_view(request):
    form = BlogForm(request.POST, request.FILES or None)
    if form.is_valid():
        form.save()
        return HttpResponseRedirect(reverse('pw:blog'))

    context = {'form': form, 'tarefas': Blog.objects.all()}
    return render(request, 'portfolio/blog.html', context)


def quizz_page_view(request):
    context = {'resultados': PontuacaoQuizz.objects.all()}
    if request.method == 'POST':
        n = request.POST['nome']
        p = pontuacao_quizz(request)
        r = PontuacaoQuizz(nome=n, pontos=p)
        r.save()
        return HttpResponseRedirect(reverse('pw:quizz'))

    return render(request, 'portfolio/quizz.html', context)


def pontuacao_quizz(request):
    pontos = 0
    if request.POST['html'] == 'linguagemProgramacao':
        pontos += 50
    if request.POST['python'] == 'linguagemProgramacao':
        pontos += 50

    return pontos


# def desenha_grafico_resultados():
# resultados_ordenados = sorted(PontuacaoQuizz.objects.all(), key=lambda objeto: objeto.pontos)
# nomes = list(PontuacaoQuizz.nome)
# print(nomes)

# criar utilizador
# user = User.objects.create_user('bm', 'bm@admin.pt', 'bm')


def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user_a = authenticate(request, username=username, password=password)

        if user_a is not None:
            login(request, user_a)
            return HttpResponseRedirect(reverse('pw:home'))
        else:
            messages.error(request, 'Credenciais invalidas.')

    return render(request, 'portfolio/login.html')


def logout_view(request):
    logout(request)
    return render(request, 'portfolio/login.html')


@login_required
def disciplina_page_view(request):
    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse('pw:login'))

    form_d = DisciplinaForm(request.POST or None)
    if form_d.is_valid():
        form_d.save()
        return HttpResponseRedirect(reverse('pw:disciplina'))

    context = {'form': form_d, 'tarefas': Blog.objects.all()}
    return render(request, 'portfolio/disciplinaNew.html', context)


def licenciatura_page_view(request):
    lista_d = Disciplina.objects.all()
    # queryset = Disciplina.objects.filter(ano=1, semestre=2)

    context = {'lista': lista_d}

    return render(request, 'portfolio/licenciatura.html', context)


@login_required
def novo_projeto_page_view(request):
    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse('pw:login'))

    form_np = ProjetoForm(request.POST, request.FILES or None)
    if form_np.is_valid():
        form_np.save()
        return HttpResponseRedirect(reverse('pw:projetos'))

    context = {'form': form_np, 'tarefas': Projeto.objects.all()}
    return render(request, 'portfolio/projetoNew.html', context)


def projetos_page_view(request):
    lista_p = Projeto.objects.all()
    # queryset = Disciplina.objects.filter(ano=1, semestre=2)

    context = {'list_p': lista_p}

    return render(request, 'portfolio/projetos.html', context)
