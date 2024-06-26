# Generated by Django 3.2.16 on 2024-05-06 23:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('professor', '0002_auto_20240506_2007'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='doutorado',
            name='data_qualificacao',
        ),
        migrations.AlterField(
            model_name='doutorado',
            name='doutorado',
            field=models.BooleanField(default=1, verbose_name='Tem Doutorado?'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='doutorado',
            name='doutorado_ano',
            field=models.IntegerField(blank=True, null=True, verbose_name='Ano do Título:'),
        ),
    ]
