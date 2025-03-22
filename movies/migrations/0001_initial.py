# Generated by Django 5.1.7 on 2025-03-22 14:41

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Pelicula',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=200, verbose_name='Título')),
                ('descripcion', models.TextField(verbose_name='Descripción')),
                ('año_lanzamiento', models.PositiveIntegerField(verbose_name='Año de Lanzamiento')),
                ('genero', models.CharField(choices=[('ACC', 'Accion'), ('COM', 'Comedia'), ('DRA', 'Drama'), ('TER', 'Terror'), ('SCI', 'Ciencia Ficcion'), ('ROM', 'Romance'), ('ANI', 'Animacion'), ('DOC', 'Documental'), ('OTH', 'Otro')], max_length=3, verbose_name='Género')),
                ('duracion', models.PositiveIntegerField(verbose_name='Duración (en minutos)')),
                ('director', models.CharField(max_length=100, verbose_name='Director')),
                ('actores_principales', models.CharField(max_length=300, verbose_name='Actores Principales')),
                ('calificacion', models.FloatField(verbose_name='Calificación (0-10)')),
                ('imagen', models.ImageField(blank=True, null=True, upload_to='peliculas/', verbose_name='Poster de la Película')),
                ('fecha_creacion', models.DateTimeField(auto_now_add=True, verbose_name='Fecha de Creación')),
                ('fecha_actualizacion', models.DateTimeField(auto_now=True, verbose_name='Fecha de Actualización')),
            ],
            options={
                'verbose_name': 'Película',
                'verbose_name_plural': 'Películas',
                'ordering': ['-fecha_creacion'],
            },
        ),
    ]
