# Generated by Django 3.2.16 on 2023-06-01 13:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('matricula', '0045_alter_probatorio_aluno'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='examelinguas',
            name='probatorio',
        ),
        migrations.AddField(
            model_name='examelinguas',
            name='probatorio',
            field=models.ManyToManyField(related_name='probatorio_exame_linguas', to='matricula.Probatorio'),
        ),
    ]
