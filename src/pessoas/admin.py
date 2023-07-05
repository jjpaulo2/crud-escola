from typing import Tuple

from django.contrib import admin
from django.http.request import HttpRequest
from django.db.models import QuerySet

from pessoas.models import Aluno, Professor
from pessoas.base.admin import PessoaGenericaAdmin


@admin.register(Aluno)
class AlunoAdmin(PessoaGenericaAdmin):
    actions = (
        'alterar_estado_matricula',
    )

    @property
    def list_display(self) -> Tuple[str]:
        original = super().list_display
        return (
            *original,
            'matriculado'
        )
    
    @property
    def list_filter(self) -> Tuple[str]:
        original = super().list_filter
        return (
            *original,
            'matriculado'
        )
    
    @admin.action(description='alterar estado da matrícula')
    def alterar_estado_matricula(self, request: HttpRequest, queryset: QuerySet[Aluno]):
        for aluno in queryset:
            aluno.matriculado = (not aluno.matriculado)
            aluno.save()


@admin.register(Professor)
class ProfessorAdmin(PessoaGenericaAdmin):
    actions = (
        'alterar_titulo_coordenador',
    )

    @property
    def list_display(self) -> Tuple[str]:
        original = super().list_display
        return (
            *original,
            'coordenador'
        )
    
    @property
    def list_filter(self) -> Tuple[str]:
        original = super().list_filter
        return (
            *original,
            'coordenador'
        )
    
    @admin.action(description='alterar título de coordenador')
    def alterar_titulo_coordenador(self, request: HttpRequest, queryset: QuerySet[Professor]):
        for professor in queryset:
            professor.coordenador = (not professor.coordenador)
            professor.save()


admin.site.disable_action("delete_selected")
