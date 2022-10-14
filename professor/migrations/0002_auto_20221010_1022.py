# Generated by Django 3.2.15 on 2022-10-10 13:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('professor', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='professor',
            name='tipo_trab',
        ),
        migrations.AddField(
            model_name='professor',
            name='tipo_docente',
            field=models.CharField(blank=True, choices=[('Permanente', 'Permanente'), ('Colaborador', 'Colaborador'), ('Coorientador', 'Coorientador'), ('Visitante', 'Visitante')], max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='posdoutorado',
            name='ano_fim',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='posdoutorado',
            name='ano_inicio',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='posdoutorado',
            name='concluido',
            field=models.BooleanField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='posdoutorado',
            name='instituicao',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='posdoutorado',
            name='pais',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='professor',
            name='cpf',
            field=models.CharField(blank=True, max_length=14, null=True),
        ),
        migrations.AlterField(
            model_name='professor',
            name='dt_nascimento',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='professor',
            name='identidade',
            field=models.CharField(blank=True, max_length=12, null=True),
        ),
        migrations.AlterField(
            model_name='professor',
            name='identidade_orgao',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='professor',
            name='identidade_uf',
            field=models.CharField(blank=True, max_length=2, null=True),
        ),
        migrations.AlterField(
            model_name='professor',
            name='nacionalidade',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='professor',
            name='naturalidade',
            field=models.CharField(blank=True, max_length=2, null=True),
        ),
        migrations.AlterField(
            model_name='professor',
            name='sexo',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='trabalho',
            name='admissao',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='trabalho',
            name='categoria',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='trabalho',
            name='email',
            field=models.EmailField(blank=True, max_length=254, null=True),
        ),
        migrations.AlterField(
            model_name='trabalho',
            name='setor',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='trabalho',
            name='telefone',
            field=models.CharField(blank=True, max_length=15, null=True),
        ),
    ]
