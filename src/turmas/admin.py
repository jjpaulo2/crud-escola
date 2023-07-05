from django.contrib import admin
from turmas.models import Turma, Periodo, Disciplina, CursoDaDisciplina


admin.site.register(Turma)
admin.site.register(Periodo)
admin.site.register(Disciplina)
admin.site.register(CursoDaDisciplina)
