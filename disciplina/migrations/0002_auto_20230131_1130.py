# Generated by Django 3.2.16 on 2023-01-31 14:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('professor', '0001_initial'),
        ('disciplina', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='disciplinaofertada',
            name='disciplina',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='disciplina_ofertada_disciplina', to='disciplina.disciplina', verbose_name='Disciplina'),
        ),
        migrations.AlterField(
            model_name='disciplinaofertada',
            name='professor',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='professor.professor', verbose_name='Professor'),
        ),
    ]