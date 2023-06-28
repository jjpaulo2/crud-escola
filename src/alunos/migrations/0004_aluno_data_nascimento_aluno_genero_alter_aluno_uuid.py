# Generated by Django 4.2.2 on 2023-06-27 22:47

import datetime
from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('alunos', '0003_delete_alunoexemplo'),
    ]

    operations = [
        migrations.AddField(
            model_name='aluno',
            name='data_nascimento',
            field=models.DateField(default=datetime.datetime(2023, 6, 27, 22, 47, 49, 701740)),
        ),
        migrations.AddField(
            model_name='aluno',
            name='genero',
            field=models.IntegerField(choices=[(1, 'Masculino'), (2, 'Feminino'), (3, 'Não informado')], default=1),
        ),
        migrations.AlterField(
            model_name='aluno',
            name='uuid',
            field=models.UUIDField(default=uuid.UUID('6b5681d2-c586-445c-b876-4cc9f9be1c8d')),
        ),
    ]
