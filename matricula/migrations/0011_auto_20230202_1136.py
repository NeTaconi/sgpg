# Generated by Django 3.2.16 on 2023-02-02 14:36

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('matricula', '0010_auto_20230202_1134'),
    ]

    operations = [
        migrations.AlterField(
            model_name='probatorio',
            name='data_inscricao',
            field=models.DateField(default=datetime.datetime(2023, 2, 2, 11, 36, 25, 325963)),
        ),
        migrations.AlterField(
            model_name='trabalhofinal',
            name='matricula',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='matricula_trabalho_final', to='matricula.matricula'),
        ),
        migrations.AlterField(
            model_name='trabalhofinal',
            name='probatorio',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='probatorio_trabalho_final', to='matricula.probatorio'),
        ),
    ]
