# Generated by Django 3.2.15 on 2022-10-10 12:21

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
            name='PosDoutorado',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('concluido', models.BooleanField()),
                ('ano_inicio', models.IntegerField()),
                ('ano_fim', models.IntegerField()),
                ('instituicao', models.CharField(max_length=200)),
                ('pais', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Trabalho',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('instituicao', models.CharField(max_length=200)),
                ('setor', models.CharField(max_length=200)),
                ('admissao', models.DateField()),
                ('cargo', models.CharField(max_length=200)),
                ('telefone', models.CharField(max_length=15)),
                ('categoria', models.CharField(max_length=200)),
                ('email', models.EmailField(max_length=254)),
            ],
        ),
        migrations.CreateModel(
            name='Professor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=200)),
                ('sexo', models.CharField(max_length=50)),
                ('dt_nascimento', models.DateField()),
                ('nacionalidade', models.CharField(max_length=100)),
                ('naturalidade', models.CharField(max_length=2)),
                ('cpf', models.CharField(max_length=14)),
                ('identidade', models.CharField(max_length=12)),
                ('identidade_uf', models.CharField(max_length=2)),
                ('identidade_orgao', models.CharField(max_length=100)),
                ('tipo_trab', models.CharField(max_length=100)),
                ('slug', models.SlugField(max_length=250, unique_for_date='dt_cadastro')),
                ('updated', models.DateTimeField(auto_now=True)),
                ('cadastrado_por', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='professor_cadastrado_por', to=settings.AUTH_USER_MODEL)),
                ('endereco', models.OneToOneField(on_delete=django.db.models.deletion.DO_NOTHING, to='aluno.endereco')),
                ('graduacao', models.OneToOneField(null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='aluno.graduacao')),
                ('pos_doutorado', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='professor_pos_doutorado', to='professor.posdoutorado')),
                ('titulacao', models.OneToOneField(on_delete=django.db.models.deletion.DO_NOTHING, to='aluno.titulacao')),
                ('trabalho', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='professor_trabalho', to='professor.trabalho')),
            ],
        ),
    ]
