# Generated by Django 3.2.15 on 2022-10-17 15:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('professor', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Disciplina',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('codigo', models.CharField(max_length=20)),
                ('nome', models.CharField(max_length=200)),
                ('carater', models.CharField(max_length=200)),
                ('carga', models.IntegerField()),
                ('creditos', models.IntegerField()),
                ('nivel', models.CharField(max_length=100)),
                ('tipo', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='DisciplinaOfertada',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ano', models.IntegerField()),
                ('semestre', models.IntegerField()),
                ('disciplina', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='disciplina_ofertada_disciplina', to='disciplina.disciplina')),
                ('professor', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='professor.professor')),
            ],
        ),
    ]
