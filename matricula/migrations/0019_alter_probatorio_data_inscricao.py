# Generated by Django 3.2.16 on 2023-02-16 11:29

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('matricula', '0018_auto_20230216_0740'),
    ]

    operations = [
        migrations.AlterField(
            model_name='probatorio',
            name='data_inscricao',
            field=models.DateField(default=datetime.datetime(2023, 2, 16, 8, 29, 45, 219549), verbose_name='Data da inscrição:'),
        ),
    ]
