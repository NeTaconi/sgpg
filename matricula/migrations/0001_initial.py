# Generated by Django 3.2.16 on 2023-01-05 14:49

import datetime
from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('aluno', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('disciplina', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Curso',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('curso', models.CharField(choices=[('Mestrado', 'Mestrado'), ('Doutorado', 'Doutorado')], max_length=200)),
                ('orientador', models.CharField(max_length=200)),
                ('coorientador', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Matricula',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('numero', models.CharField(max_length=10)),
                ('requisita_bolsa', models.BooleanField()),
                ('status', models.CharField(choices=[('Ativo', 'Ativo'), ('Titulado', 'Titulado'), ('Jubilado', 'Jubilado'), ('Abandono', 'Abandono')], default='Ativo', max_length=20)),
                ('slug', models.SlugField(max_length=250, unique_for_date='dt_cadastro')),
                ('updated', models.DateTimeField(auto_now=True)),
                ('dt_cadastro', models.DateTimeField(auto_now=True)),
                ('cadastrado_por', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='matricula_cadastrado_por', to=settings.AUTH_USER_MODEL)),
                ('curso', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='matricula_curso', to='matricula.curso')),
            ],
        ),
        migrations.CreateModel(
            name='Probatorio',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data_inscricao', models.DateField(default=datetime.datetime(2023, 1, 5, 11, 49, 4, 321548))),
                ('nota', models.FloatField(null=True, validators=[django.core.validators.MaxValueValidator(100), django.core.validators.MinValueValidator(0)])),
                ('probatorio', models.BooleanField(default=True)),
                ('slug', models.SlugField(max_length=250, unique_for_date='dt_cadastro')),
                ('updated', models.DateTimeField(auto_now=True)),
                ('dt_cadastro', models.DateTimeField(auto_now=True)),
                ('aluno', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='probatorio_aluno', to='aluno.aluno')),
                ('cadastrado_por', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='probatorio_cadastrado_por', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='TrabalhoFinal',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=200)),
                ('data', models.DateField()),
                ('resumo', models.TextField()),
                ('resultado', models.FloatField(validators=[django.core.validators.MaxValueValidator(100), django.core.validators.MinValueValidator(0)])),
                ('diploma', models.BooleanField()),
                ('dt_diploma', models.DateField()),
                ('versao_final', models.BooleanField()),
                ('dt_versao', models.DateField()),
                ('slug', models.SlugField(max_length=250, unique_for_date='dt_cadastro')),
                ('updated', models.DateTimeField(auto_now=True)),
                ('cadastrado_por', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='trabalho_final_cadastrado_por', to=settings.AUTH_USER_MODEL)),
                ('matricula', models.OneToOneField(null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='matricula_trabalho_final', to='matricula.matricula')),
                ('probatorio', models.OneToOneField(null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='probatorio_trabalho_final', to='matricula.probatorio')),
            ],
        ),
        migrations.AddField(
            model_name='matricula',
            name='probatorio',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='matricula_probatorio', to='matricula.probatorio'),
        ),
        migrations.CreateModel(
            name='InscricaoProbatorio',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nota', models.FloatField(validators=[django.core.validators.MaxValueValidator(100), django.core.validators.MinValueValidator(0)])),
                ('slug', models.SlugField(max_length=250, unique_for_date='dt_cadastro')),
                ('updated', models.DateTimeField(auto_now=True)),
                ('cadastrado_por', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='inscricao_probatorio_cadastrado_por', to=settings.AUTH_USER_MODEL)),
                ('disciplina_ofertada', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='inscricao_probatorio_disciplina_ofertada', to='disciplina.disciplinaofertada')),
                ('probatorio', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='inscricao_probatorio_probatorio', to='matricula.probatorio')),
            ],
        ),
        migrations.CreateModel(
            name='Inscricao',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nota', models.FloatField(validators=[django.core.validators.MaxValueValidator(100), django.core.validators.MinValueValidator(0)])),
                ('slug', models.SlugField(max_length=250, unique_for_date='dt_cadastro')),
                ('updated', models.DateTimeField(auto_now=True)),
                ('cadastrado_por', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='inscricao_cadastrado_por', to=settings.AUTH_USER_MODEL)),
                ('disciplina_ofertada', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='inscricao_disciplina_ofertada', to='disciplina.disciplinaofertada')),
                ('matricula', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='inscricao_matricula', to='matricula.matricula')),
            ],
        ),
        migrations.CreateModel(
            name='Bolsa',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=200)),
                ('agencia', models.CharField(max_length=200)),
                ('dt_inicio', models.DateField()),
                ('iniciacao_cientifica', models.BooleanField()),
                ('dt_cadastro', models.DateTimeField(auto_now=True)),
                ('matricula', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='bolsa_matricula', to='matricula.matricula')),
            ],
        ),
        migrations.CreateModel(
            name='Afastamento',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('motivo', models.CharField(max_length=200)),
                ('saida', models.DateField()),
                ('retorno', models.DateField()),
                ('dt_cadastro', models.DateTimeField(auto_now=True)),
                ('matricula', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='afastamento_matricula', to='matricula.matricula')),
            ],
        ),
    ]
