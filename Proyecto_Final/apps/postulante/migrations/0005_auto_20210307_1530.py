# Generated by Django 3.1.7 on 2021-03-07 18:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('postulante', '0004_auto_20210307_1137'),
    ]

    operations = [
        migrations.AlterField(
            model_name='postulante',
            name='comentario',
            field=models.CharField(max_length=500, null=True),
        ),
        migrations.AlterField(
            model_name='postulante',
            name='fecha',
            field=models.DateTimeField(auto_now=True),
        ),
    ]