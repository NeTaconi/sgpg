# Generated by Django 3.2.16 on 2023-02-02 14:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('professor', '0001_initial'),
        ('evento', '0002_auto_20230130_0941'),
    ]

    operations = [
        migrations.AlterField(
            model_name='participante',
            name='participante_professor',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='participante_professor', to='professor.professor'),
        ),
    ]
