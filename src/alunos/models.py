from uuid import uuid4
from django.utils.timezone import now
from django.db import models


class ModeloGenerico(models.Model):
    GENEROS_POSSIVEIS = [
        (1, "Masculino"),
        (2, "Feminino"),
        (3, "Não informado")
    ]

    uuid = models.UUIDField(
        default=uuid4(),
        verbose_name='ID'
    )
    nome = models.CharField(
        max_length=255
    )
    sobrenome = models.CharField(
        max_length=255,
        null=True,
        blank=True
    )
    genero = models.IntegerField(
        choices=GENEROS_POSSIVEIS,
        default=1,
        verbose_name='gênero'
    )
    data_nascimento = models.DateField(
        default=now,
        verbose_name='data de nascimento'
    )
    email = models.EmailField(
        verbose_name='e-mail'
    )
    telefone = models.CharField(
        max_length=11,
        null=True,
        blank=True
    )

    class Meta:
        abstract = True


class Aluno(ModeloGenerico):
    observacao = models.TextField(
        verbose_name='observação',
        null=True,
        blank=True
    )
    matriculado = models.BooleanField(
        help_text='a matricula do aluno está ativa?',
        default=False
    )
    
    def __str__(self):
        return f'Aluno #{self.pk} - {self.nome}'
    