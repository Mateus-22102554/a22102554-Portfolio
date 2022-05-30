"""config URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf.urls.static import static
from django.urls import path

from projeto import settings
from . import views

app_name = 'pw'

urlpatterns = [
    path('', views.capa_page_view, name='capa'),
    path('capa', views.capa_page_view, name='capa'),
    path('home', views.home_page_view, name='home'),
    path('layout', views.layout_page_view, name='layout'),
    path('projetos', views.projetos_page_view, name='projetos'),
    path('apresentacao', views.apresentacao_page_view, name='apresentacao'),
    path('competencias', views.competencias_page_view, name='competencias'),
    path('formacao', views.formacao_page_view, name='formacao'),
    path('licenciatura', views.licenciatura_page_view, name='licenciatura'),
    path('blog', views.blog_page_view, name='blog'),
    path('quizz', views.quizz_page_view, name='quizz'),
    path('login', views.login_view, name='login'),
    path('logout', views.logout_view, name='logout'),
    path('disciplina', views.disciplina_page_view, name='disciplina'),
    path('novo_projeto', views.novo_projeto_page_view, name='novo_projeto')

]

