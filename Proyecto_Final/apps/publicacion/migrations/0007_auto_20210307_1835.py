# Generated by Django 3.1.7 on 2021-03-07 21:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('publicacion', '0006_auto_20210307_1542'),
    ]

    operations = [
        migrations.AlterField(
            model_name='publicacion',
            name='foto',
            field=models.ImageField(upload_to='media'),
        ),
    ]
