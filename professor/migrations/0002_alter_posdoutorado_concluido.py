# Generated by Django 3.2.15 on 2022-10-19 15:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('professor', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='posdoutorado',
            name='concluido',
            field=models.BooleanField(default=1),
            preserve_default=False,
        ),
    ]
