from django.contrib import admin

# Register your models here.

from .models import *

admin.site.register(Blog)
admin.site.register(PontuacaoQuizz)
admin.site.register(Disciplina)
admin.site.register(Projeto)
