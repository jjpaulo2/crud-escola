from datetime import date, timedelta
from django.contrib import admin
from django.http.request import HttpRequest
from django.db.models import QuerySet

from import_export.admin import ImportExportModelAdmin

from alunos.models import Aluno


@admin.register(Aluno)
class AlunoAdmin(ImportExportModelAdmin):
    actions = (
        'alterar_estado_matricula',
    )
    list_display = (
        'uuid',
        'nome',
        'get_data_de_nascimento',
        'get_idade',
        'email',
        'genero',
        'matriculado'
    )
    list_filter = (
        'data_nascimento',
        'genero',
        'matriculado'
    )
    search_fields = (
        'uuid',
        'nome',
        'email'
    )
    list_per_page = 50

    fieldsets = [
        (
            'Identificação',
            {
                'fields': [(
                    'nome',
                    'sobrenome'
                )],
            },
        ),
        (
            'Informações básicas',
            {
                'fields': [(
                    'genero',
                    'data_nascimento'
                )],
            },
        ),
        (
            'Informações de contato',
            {
                'fields': [(
                    'email',
                    'telefone'
                )],
            },
        ),
        (
            'Informações extras',
            {
                'classes': ['collapse'],
                'fields': ['observacao'],
            },
        ),
    ]

    @admin.display(description='idade')
    def get_idade(self, obj: Aluno) -> str:
        idade_timedelta: timedelta = date.today() - obj.data_nascimento
        idade = idade_timedelta.days // 365
        idade_str = f'{idade}'
        anos_str = 'anos' if idade > 1 else 'ano' 
        return f'{idade_str} {anos_str}'
    
    @admin.display(description='data de nascimento')
    def get_data_de_nascimento(self, obj: Aluno) -> str:
        return obj.data_nascimento.strftime('%d/%m/%Y')
    
    @admin.action(description='alterar estado da matrícula')
    def alterar_estado_matricula(self, request: HttpRequest, queryset: QuerySet[Aluno]):
        for aluno in queryset:
            aluno.matriculado = (not aluno.matriculado)
            aluno.save()


admin.site.disable_action("delete_selected")
