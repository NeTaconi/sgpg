# Generated by Django 3.2.16 on 2023-02-27 15:20

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('matricula', '0023_alter_probatorio_data_inscricao'),
    ]

    operations = [
        migrations.AlterField(
            model_name='probatorio',
            name='data_inscricao',
            field=models.DateField(default=datetime.datetime(2023, 2, 27, 12, 20, 4, 631464), verbose_name='Data da inscrição:'),
        ),
    ]