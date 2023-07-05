from uuid import uuid4
from django.utils.timezone import now
from django.db import models

from pessoas.base.models import PessoaGenerica


class Aluno(PessoaGenerica):
    matriculado = models.BooleanField(
        help_text='a matricula do aluno está ativa?',
        default=False
    )
    
    def __str__(self):
        return f'Aluno #{self.pk} - {self.nome}'
    

class Professor(PessoaGenerica):
    coordenador = models.BooleanField(
        help_text='é um coordenador atualmente?',
        default=False
    )
    
    def __str__(self):
        return f'Professor #{self.pk} - {self.nome}'
    
    class Meta:
        verbose_name = 'professor'
        verbose_name_plural = 'professores'
