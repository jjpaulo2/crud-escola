from django.db import models
from pessoas.models import Professor


class Turma(models.Model):
    nome = models.CharField(
        max_length=255
    )
    ano = models.IntegerField()

    def __str__(self):
        return f'{self.nome} - {self.ano}'


class Disciplina(models.Model):
    nome = models.CharField(
        max_length=255
    )

    def __str__(self):
        return f'{self.nome}'


class Periodo(models.Model):
    nome = models.CharField(
        max_length=255,
        null=True,
        blank=True
    )
    data_inicio = models.DateField()
    data_fim = models.DateField(
        null=True,
        blank=True
    )

    def __str__(self):
        return f'{self.nome} - {self.data_inicio} - {self.data_fim}'


class CursoDaDisciplina(models.Model):
    periodo = models.ForeignKey(
        to=Periodo,
        on_delete=models.PROTECT
    )
    disciplina = models.ForeignKey(
        to=Disciplina,
        on_delete=models.PROTECT
    )
    professor = models.ForeignKey(
        to=Professor,
        on_delete=models.PROTECT
    )
    turmas = models.ManyToManyField(
        to=Turma
    )

    def __str__(self):
        return f'{self.disciplina.nome} - {self.periodo.nome} - {self.professor.nome_completo}'
