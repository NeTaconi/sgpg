# Generated by Django 3.2.16 on 2023-02-16 10:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('aluno', '0008_aluno_foto'),
    ]

    operations = [
        migrations.AlterField(
            model_name='aluno',
            name='foto',
            field=models.ImageField(blank=True, null=True, upload_to='img'),
        ),
    ]
