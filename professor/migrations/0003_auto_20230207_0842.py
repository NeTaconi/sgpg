# Generated by Django 3.2.16 on 2023-02-07 11:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('professor', '0002_auto_20230206_0809'),
    ]

    operations = [
        migrations.AlterField(
            model_name='posdoutorado',
            name='ano_fim',
            field=models.IntegerField(blank=True, null=True, verbose_name='Ano de término:'),
        ),
        migrations.AlterField(
            model_name='posdoutorado',
            name='ano_inicio',
            field=models.IntegerField(blank=True, null=True, verbose_name='Ano de início:'),
        ),
        migrations.AlterField(
            model_name='posdoutorado',
            name='concluido',
            field=models.BooleanField(verbose_name='Concluído:'),
        ),
        migrations.AlterField(
            model_name='posdoutorado',
            name='instituicao_posdoc',
            field=models.CharField(blank=True, max_length=200, null=True, verbose_name='Instituição de Pós-doutorado:'),
        ),
        migrations.AlterField(
            model_name='posdoutorado',
            name='pais',
            field=models.CharField(blank=True, max_length=200, null=True, verbose_name='País:'),
        ),
        migrations.AlterField(
            model_name='professor',
            name='cpf',
            field=models.CharField(blank=True, max_length=14, null=True, verbose_name='CPF:'),
        ),
        migrations.AlterField(
            model_name='professor',
            name='dt_nascimento',
            field=models.DateField(blank=True, null=True, verbose_name='Data de nascimento:'),
        ),
        migrations.AlterField(
            model_name='professor',
            name='estrangeiro',
            field=models.BooleanField(default=False, verbose_name='Estrangeiro:'),
        ),
        migrations.AlterField(
            model_name='professor',
            name='identidade',
            field=models.CharField(blank=True, max_length=12, null=True, verbose_name='Identidade:'),
        ),
        migrations.AlterField(
            model_name='professor',
            name='identidade_orgao',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='Orgão Expeditor:'),
        ),
        migrations.AlterField(
            model_name='professor',
            name='identidade_uf',
            field=models.CharField(blank=True, max_length=2, null=True, verbose_name='UF:'),
        ),
        migrations.AlterField(
            model_name='professor',
            name='nacionalidade',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='Nacionalidade:'),
        ),
        migrations.AlterField(
            model_name='professor',
            name='naturalidade',
            field=models.CharField(blank=True, max_length=2, null=True, verbose_name='Naturalidade:'),
        ),
        migrations.AlterField(
            model_name='professor',
            name='nome',
            field=models.CharField(max_length=200, verbose_name='Nome:'),
        ),
        migrations.AlterField(
            model_name='professor',
            name='sexo',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='Sexo:'),
        ),
        migrations.AlterField(
            model_name='professor',
            name='tipo_docente',
            field=models.CharField(blank=True, choices=[('Permanente', 'Permanente'), ('Colaborador', 'Colaborador'), ('Coorientador', 'Coorientador'), ('Visitante', 'Visitante'), ('Pos Doutor', 'Pós Doutor')], max_length=100, null=True, verbose_name='Tipo de docente:'),
        ),
        migrations.AlterField(
            model_name='trabalho',
            name='admissao',
            field=models.DateField(blank=True, null=True, verbose_name='Admissão:'),
        ),
        migrations.AlterField(
            model_name='trabalho',
            name='cargo',
            field=models.CharField(max_length=200, verbose_name='Cargo:'),
        ),
        migrations.AlterField(
            model_name='trabalho',
            name='categoria',
            field=models.CharField(blank=True, max_length=200, null=True, verbose_name='Categoria:'),
        ),
        migrations.AlterField(
            model_name='trabalho',
            name='email',
            field=models.EmailField(blank=True, max_length=254, null=True, verbose_name='Email:'),
        ),
        migrations.AlterField(
            model_name='trabalho',
            name='instituicao_trabalho',
            field=models.CharField(max_length=200, verbose_name='Instituição:'),
        ),
        migrations.AlterField(
            model_name='trabalho',
            name='setor',
            field=models.CharField(blank=True, max_length=200, null=True, verbose_name='Setor:'),
        ),
        migrations.AlterField(
            model_name='trabalho',
            name='telefone',
            field=models.CharField(blank=True, max_length=15, null=True, verbose_name='Telefone:'),
        ),
    ]