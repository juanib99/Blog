# Generated by Django 4.0.4 on 2022-06-26 03:22

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='blog',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, unique=True)),
                ('titulo', models.CharField(max_length=100)),
                ('subtitulo', models.CharField(max_length=100)),
                ('texto', models.TextField()),
                ('autor', models.CharField(max_length=40)),
                ('fecha', models.DateField()),
                ('imagen', models.ImageField(upload_to='imagenes/')),
            ],
        ),
    ]
