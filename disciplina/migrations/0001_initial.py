# Generated by Django 3.2.16 on 2024-05-06 18:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Disciplina',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('codigo', models.CharField(max_length=20)),
                ('nome', models.CharField(max_length=200)),
                ('carater', models.CharField(blank=True, max_length=200, null=True)),
                ('carga', models.IntegerField()),
                ('creditos', models.IntegerField()),
                ('nivel', models.CharField(blank=True, max_length=100, null=True)),
                ('tipo', models.CharField(blank=True, max_length=100, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='DisciplinaOfertada',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ano', models.IntegerField()),
                ('semestre', models.IntegerField()),
                ('disciplina', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='disciplina_ofertada_disciplina', to='disciplina.disciplina', verbose_name='Disciplina')),
            ],
        ),
    ]
