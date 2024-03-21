# Generated by Django 4.2.3 on 2023-07-31 17:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Autor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=30)),
                ('apellidos', models.CharField(max_length=50)),
                ('correo', models.EmailField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Editor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=30)),
                ('domicilio', models.CharField(max_length=50)),
                ('ciudad', models.CharField(max_length=30)),
                ('provincia', models.CharField(max_length=30)),
                ('pais', models.CharField(max_length=30)),
                ('web', models.URLField(max_length=80)),
            ],
        ),
        migrations.CreateModel(
            name='Libro',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=30)),
                ('precio', models.FloatField()),
                ('existencias', models.IntegerField()),
                ('autor', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='aplicacion2.autor')),
                ('editor', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='aplicacion2.editor')),
            ],
        ),
    ]
