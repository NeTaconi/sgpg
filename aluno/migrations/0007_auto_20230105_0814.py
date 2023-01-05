# Generated by Django 3.2.16 on 2023-01-05 11:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('aluno', '0006_auto_20221101_1012'),
    ]

    operations = [
        migrations.CreateModel(
            name='EnsinoMedio',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ensino_medio_instituicao', models.CharField(blank=True, max_length=200, null=True)),
                ('ensino_medio_ano_inicio', models.IntegerField(blank=True, null=True)),
                ('ensino_medio_ano_conclusao', models.IntegerField(blank=True, null=True)),
                ('ensino_medio_municipio', models.CharField(blank=True, max_length=200, null=True)),
            ],
        ),
        migrations.AddField(
            model_name='aluno',
            name='ensino_medio',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='aluno_ensino_medio', to='aluno.ensinomedio'),
        ),
    ]
