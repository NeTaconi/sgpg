# Generated by Django 3.2.16 on 2023-03-24 13:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('config', '0016_grau'),
        ('matricula', '0036_probatorio_grau'),
    ]

    operations = [
        migrations.AddField(
            model_name='matricula',
            name='grau',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='matricula_grau', to='config.grau', verbose_name='Grau de Aplicação:'),
            preserve_default=False,
        ),
    ]
