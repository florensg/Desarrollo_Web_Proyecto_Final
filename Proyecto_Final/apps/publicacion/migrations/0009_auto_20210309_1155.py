# Generated by Django 3.1.7 on 2021-03-09 14:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('publicacion', '0008_contador'),
    ]

    operations = [
        migrations.RenameField(
            model_name='contador',
            old_name='Publicacion',
            new_name='publicacion',
        ),
    ]
