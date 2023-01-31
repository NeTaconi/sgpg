# Generated by Django 3.2.16 on 2023-01-31 15:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('config', '0002_sexo'),
        ('aluno', '0003_alter_aluno_naturalidade'),
    ]

    operations = [
        migrations.AlterField(
            model_name='aluno',
            name='sexo',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='config.sexo', verbose_name='Sexo:'),
        ),
    ]
