# Generated by Django 3.2.16 on 2023-03-01 12:12

import colorful.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('config', '0009_auto_20230301_0844'),
    ]

    operations = [
        migrations.AddField(
            model_name='statusoptions',
            name='cor',
            field=colorful.fields.RGBColorField(default='#000000'),
        ),
        migrations.AddField(
            model_name='vinculo',
            name='cor',
            field=colorful.fields.RGBColorField(default='#000000'),
        ),
    ]
