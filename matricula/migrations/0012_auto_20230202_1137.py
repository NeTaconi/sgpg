# Generated by Django 3.2.16 on 2023-02-02 14:37

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('matricula', '0011_auto_20230202_1136'),
    ]

    operations = [
        migrations.AlterField(
            model_name='inscricao',
            name='matricula',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='inscricao_matricula', to='matricula.matricula'),
        ),
        migrations.AlterField(
            model_name='probatorio',
            name='data_inscricao',
            field=models.DateField(default=datetime.datetime(2023, 2, 2, 11, 37, 11, 117155)),
        ),
    ]
