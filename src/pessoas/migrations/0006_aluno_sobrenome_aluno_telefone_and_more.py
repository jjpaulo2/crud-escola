# Generated by Django 4.2.2 on 2023-06-27 20:38

from django.db import migrations, models
import django.utils.timezone
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('pessoas', '0005_alter_aluno_data_nascimento_alter_aluno_uuid'),
    ]

    operations = [
        migrations.AddField(
            model_name='aluno',
            name='sobrenome',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='aluno',
            name='telefone',
            field=models.CharField(blank=True, max_length=11, null=True),
        ),
        migrations.AlterField(
            model_name='aluno',
            name='data_nascimento',
            field=models.DateField(default=django.utils.timezone.now, verbose_name='data de nascimento'),
        ),
        migrations.AlterField(
            model_name='aluno',
            name='email',
            field=models.EmailField(max_length=254, verbose_name='e-mail'),
        ),
        migrations.AlterField(
            model_name='aluno',
            name='genero',
            field=models.IntegerField(choices=[(1, 'Masculino'), (2, 'Feminino'), (3, 'Não informado')], default=1, verbose_name='gênero'),
        ),
        migrations.AlterField(
            model_name='aluno',
            name='uuid',
            field=models.UUIDField(default=uuid.UUID('2ce96ab8-7c67-453d-8c99-cfcdf4e16cd6'), verbose_name='ID'),
        ),
    ]
