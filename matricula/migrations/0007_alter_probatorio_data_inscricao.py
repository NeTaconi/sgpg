# Generated by Django 3.2.16 on 2023-01-31 15:59

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('matricula', '0006_alter_probatorio_data_inscricao'),
    ]

    operations = [
        migrations.AlterField(
            model_name='probatorio',
            name='data_inscricao',
            field=models.DateField(default=datetime.datetime(2023, 1, 31, 12, 59, 39, 577874)),
        ),
    ]
