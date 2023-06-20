from uuid import uuid4
from django.db import models


class ModeloGenerico(models.Model):
    uuid = models.UUIDField(
        default=uuid4()
    )
    nome = models.CharField(
        max_length=255
    )

    class Meta:
        abstract = True


class Aluno(ModeloGenerico):
    email = models.EmailField()

    def __str__(self):
        return f'Aluno #{self.pk} - {self.nome}'
    