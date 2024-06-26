# Generated by Django 3.2.16 on 2024-05-06 18:17

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('aluno', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('config', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Afastamento',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('motivo', models.CharField(max_length=200, verbose_name='Motivo:')),
                ('saida', models.DateField(verbose_name='Saída:')),
                ('retorno', models.DateField(verbose_name='Retorno:')),
                ('dt_cadastro', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Bolsa',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=200, verbose_name='Bolsa:')),
                ('agencia', models.CharField(max_length=200, verbose_name='Agência:')),
                ('dt_inicio', models.DateField(verbose_name='Data de início:')),
                ('iniciacao_cientifica', models.BooleanField(verbose_name='Iniciação científica:')),
                ('dt_cadastro', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Curso',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('curso', models.CharField(choices=[('Mestrado', 'Mestrado'), ('Doutorado', 'Doutorado')], max_length=200, verbose_name='Curso:')),
                ('orientador', models.CharField(max_length=200, verbose_name='Orientador:')),
                ('coorientador', models.CharField(max_length=200, verbose_name='Coorientador:')),
            ],
        ),
        migrations.CreateModel(
            name='ExameLinguas',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nota', models.FloatField(validators=[django.core.validators.MaxValueValidator(100), django.core.validators.MinValueValidator(0)])),
                ('dt_nota', models.DateField(auto_now=True)),
            ],
            options={
                'verbose_name': 'Exame de Lingua',
                'verbose_name_plural': 'Exames de Linguas',
            },
        ),
        migrations.CreateModel(
            name='Inscricao',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nota', models.FloatField(blank=True, null=True, validators=[django.core.validators.MaxValueValidator(100), django.core.validators.MinValueValidator(0)])),
                ('situacao', models.CharField(choices=[('Cursando', 'Cursando'), ('Aprovado', 'Aprovado'), ('Reprovado', 'Reprovado'), ('Trancado', 'Trancado')], default=('Cursando', 'Cursando'), max_length=200)),
                ('slug', models.SlugField(max_length=250, unique_for_date='dt_cadastro')),
                ('updated', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name_plural': 'Inscrições',
            },
        ),
        migrations.CreateModel(
            name='InscricaoProbatorio',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('situacao', models.CharField(choices=[('Cursando', 'Cursando'), ('Aprovado', 'Aprovado'), ('Reprovado', 'Reprovado'), ('Trancado', 'Trancado')], default=('Cursando', 'Cursando'), max_length=200)),
                ('nota', models.FloatField(blank=True, null=True, validators=[django.core.validators.MaxValueValidator(100), django.core.validators.MinValueValidator(0)])),
                ('slug', models.SlugField(max_length=250, unique_for_date='dt_cadastro')),
                ('updated', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Matricula',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('numero', models.CharField(max_length=10, verbose_name='Número:')),
                ('dt_matricula', models.DateField(verbose_name='Data de Matrícula:')),
                ('requisita_bolsa', models.BooleanField(verbose_name='Requisita bolsa:')),
                ('cotista', models.BooleanField(verbose_name='Cotista:')),
                ('status', models.CharField(choices=[('Ativo', 'Ativo'), ('Titulado', 'Titulado'), ('Jubilado', 'Jubilado'), ('Abandono', 'Abandono')], default='Ativo', max_length=20, verbose_name='Status:')),
                ('slug', models.SlugField(max_length=250, unique_for_date='dt_cadastro')),
                ('updated', models.DateTimeField(auto_now=True)),
                ('dt_cadastro', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name': 'matricula',
            },
        ),
        migrations.CreateModel(
            name='Nota',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nota', models.FloatField(validators=[django.core.validators.MaxValueValidator(100), django.core.validators.MinValueValidator(0)])),
                ('dt_nota', models.DateField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Orientacao',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tipo', models.CharField(choices=[('Orientador', 'Orientador'), ('Coorientador', 'Coorientador')], max_length=200)),
                ('professor_externo', models.BooleanField()),
            ],
            options={
                'verbose_name_plural': 'Orientações',
            },
        ),
        migrations.CreateModel(
            name='Probatorio',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data_inscricao', models.DateField(verbose_name='Data da inscrição:')),
                ('probatorio', models.BooleanField(default=True)),
                ('slug', models.SlugField(max_length=250, unique_for_date='dt_cadastro')),
                ('updated', models.DateTimeField(auto_now=True)),
                ('dt_cadastro', models.DateTimeField(auto_now=True)),
                ('aluno', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='probatorio_aluno', to='aluno.aluno', verbose_name='Aluno:')),
                ('cadastrado_por', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='probatorio_cadastrado_por', to=settings.AUTH_USER_MODEL)),
                ('grau', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='probatorio_grau', to='config.grau', verbose_name='Grau de Aplicação:')),
                ('linha_pesquisa', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='config.linhapesquisa')),
                ('nota', models.OneToOneField(null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='probatorio_nota', to='matricula.nota', verbose_name='Nota:')),
            ],
        ),
        migrations.CreateModel(
            name='VersaoFinal',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('versao_final', models.BooleanField()),
                ('dt_versao', models.DateField(auto_now=True)),
            ],
            options={
                'verbose_name_plural': 'Versões Finais',
            },
        ),
        migrations.CreateModel(
            name='TrabalhoFinal',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=200)),
                ('resumo', models.TextField()),
                ('diploma', models.BooleanField(blank=True, null=True)),
                ('dt_diploma', models.DateField(blank=True, null=True)),
                ('slug', models.SlugField(max_length=250, unique_for_date='dt_cadastro')),
                ('dt_cadastro', models.DateTimeField(auto_now=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('cadastrado_por', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='trabalho_final_cadastrado_por', to=settings.AUTH_USER_MODEL)),
                ('matricula', models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='matricula_trabalho_final', to='matricula.matricula')),
                ('nota', models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='nota_trabalho_final', to='matricula.nota')),
                ('probatorio', models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='probatorio_trabalho_final', to='matricula.probatorio')),
                ('versao_final', models.OneToOneField(null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='versao_final_trabalho_final', to='matricula.versaofinal')),
            ],
            options={
                'verbose_name_plural': 'Trabalhos Finais',
            },
        ),
    ]
