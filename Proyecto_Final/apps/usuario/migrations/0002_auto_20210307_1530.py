# Generated by Django 3.1.7 on 2021-03-07 18:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('usuario', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='usuario',
            name='cantidad_de_calificaciones',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='usuario',
            name='provincia',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='usuario',
            name='descripcion_propia',
            field=models.CharField(max_length=2000, null=True),
        ),
        migrations.AlterField(
            model_name='usuario',
            name='promedio_calificacion',
            field=models.FloatField(null=True),
        ),
    ]