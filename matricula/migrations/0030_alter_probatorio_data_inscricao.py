# Generated by Django 3.2.16 on 2023-03-01 10:33

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('matricula', '0029_alter_probatorio_data_inscricao'),
    ]

    operations = [
        migrations.AlterField(
            model_name='probatorio',
            name='data_inscricao',
            field=models.DateField(default=datetime.datetime(2023, 3, 1, 7, 33, 53, 541176), verbose_name='Data da inscrição:'),
        ),
    ]
