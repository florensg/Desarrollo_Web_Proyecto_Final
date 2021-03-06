# Generated by Django 3.1.7 on 2021-03-04 23:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Chat',
            fields=[
                ('id_chat', models.AutoField(primary_key=True, serialize=False)),
                ('estado', models.BooleanField()),
            ],
        ),
        migrations.CreateModel(
            name='Mensaje',
            fields=[
                ('id_mensaje', models.AutoField(primary_key=True, serialize=False)),
                ('mensaje', models.CharField(max_length=250, null=True)),
                ('fecha', models.DateField()),
                ('correo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='+', to='mensaje.chat')),
            ],
        ),
    ]
