# Generated by Django 4.2.2 on 2023-06-27 20:55

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('pessoas', '0007_aluno_observacao_alter_aluno_uuid'),
    ]

    operations = [
        migrations.AddField(
            model_name='aluno',
            name='matriculado',
            field=models.BooleanField(default=False, help_text='a matricula do aluno está ativa?'),
        ),
        migrations.AlterField(
            model_name='aluno',
            name='observacao',
            field=models.TextField(blank=True, null=True, verbose_name='observação'),
        ),
        migrations.AlterField(
            model_name='aluno',
            name='uuid',
            field=models.UUIDField(default=uuid.UUID('6c87d009-5aab-4939-9181-2458babc9412'), verbose_name='ID'),
        ),
    ]
