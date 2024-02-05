# Generated by Django 3.2.16 on 2024-01-22 22:51

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('matricula', '0046_auto_20230601_1058'),
    ]

    operations = [
        migrations.AddField(
            model_name='inscricaoprobatorio',
            name='situação',
            field=models.CharField(choices=[('Cursando', 'Cursando'), ('Aprovado', 'Aprovado'), ('Reprovado', 'Reprovado'), ('Trancado', 'Trancado')], default=('Cursando', 'Cursando'), max_length=200),
        ),
        migrations.AlterField(
            model_name='inscricaoprobatorio',
            name='nota',
            field=models.FloatField(blank=True, null=True, validators=[django.core.validators.MaxValueValidator(100), django.core.validators.MinValueValidator(0)]),
        ),
    ]