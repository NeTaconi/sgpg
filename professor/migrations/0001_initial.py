# Generated by Django 3.2.16 on 2023-01-23 14:00

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('aluno', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Colegiado',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('colegiado_membro', models.BooleanField(default=False)),
                ('colegiado_data_entrada', models.DateField(blank=True, null=True)),
                ('colegiado_data_saida', models.DateField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='PosDoutorado',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('concluido', models.BooleanField()),
                ('ano_inicio', models.IntegerField(blank=True, null=True)),
                ('ano_fim', models.IntegerField(blank=True, null=True)),
                ('instituicao_posdoc', models.CharField(blank=True, max_length=200, null=True)),
                ('pais', models.CharField(blank=True, max_length=200, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Trabalho',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('instituicao_trabalho', models.CharField(max_length=200)),
                ('setor', models.CharField(blank=True, max_length=200, null=True)),
                ('admissao', models.DateField(blank=True, null=True)),
                ('cargo', models.CharField(max_length=200)),
                ('telefone', models.CharField(blank=True, max_length=15, null=True)),
                ('categoria', models.CharField(blank=True, max_length=200, null=True)),
                ('email', models.EmailField(blank=True, max_length=254, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Professor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=200)),
                ('sexo', models.CharField(blank=True, max_length=50, null=True)),
                ('dt_nascimento', models.DateField(blank=True, null=True)),
                ('estrangeiro', models.BooleanField(default=False)),
                ('nacionalidade', models.CharField(blank=True, max_length=100, null=True)),
                ('naturalidade', models.CharField(blank=True, max_length=2, null=True)),
                ('cpf', models.CharField(blank=True, max_length=14, null=True)),
                ('identidade', models.CharField(blank=True, max_length=12, null=True)),
                ('identidade_uf', models.CharField(blank=True, max_length=2, null=True)),
                ('identidade_orgao', models.CharField(blank=True, max_length=100, null=True)),
                ('tipo_docente', models.CharField(blank=True, choices=[('Permanente', 'Permanente'), ('Colaborador', 'Colaborador'), ('Coorientador', 'Coorientador'), ('Visitante', 'Visitante'), ('Pos Doutor', 'Pós Doutor')], max_length=100, null=True)),
                ('slug', models.SlugField(max_length=250, unique_for_date='dt_cadastro')),
                ('updated', models.DateTimeField(auto_now=True)),
                ('cadastrado_por', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='professor_cadastrado_por', to=settings.AUTH_USER_MODEL)),
                ('endereco', models.OneToOneField(on_delete=django.db.models.deletion.DO_NOTHING, to='aluno.endereco')),
                ('graduacao', models.OneToOneField(null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='aluno.graduacao')),
                ('membro_colegiado', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='professor_membro_colegiado', to='professor.colegiado')),
                ('pos_doutorado', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='professor_pos_doutorado', to='professor.posdoutorado')),
                ('titulacao', models.OneToOneField(on_delete=django.db.models.deletion.DO_NOTHING, to='aluno.titulacao')),
                ('trabalho', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='professor_trabalho', to='professor.trabalho')),
            ],
        ),
    ]
