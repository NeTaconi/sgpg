# Generated by Django 3.2.16 on 2024-05-07 01:18

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('matricula', '0002_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='probatorio',
            name='nota_selecao',
            field=models.FloatField(default=1, validators=[django.core.validators.MaxValueValidator(100), django.core.validators.MinValueValidator(0)]),
            preserve_default=False,
        ),
    ]
