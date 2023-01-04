# Generated by Django 3.2.16 on 2023-01-04 12:23

import datetime
import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('matricula', '0002_alter_matricula_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='probatorio',
            name='data_inscricao',
            field=models.DateField(default=datetime.datetime(2023, 1, 4, 9, 23, 10, 604998)),
        ),
        migrations.AlterField(
            model_name='probatorio',
            name='nota',
            field=models.FloatField(null=True, validators=[django.core.validators.MaxValueValidator(100), django.core.validators.MinValueValidator(0)]),
        ),
    ]