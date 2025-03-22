from django.db import models

# Create your models here.

from django.db import models

class Pelicula(models.Model):
    # Opciones para el campo de género
    GENERO_CHOICES = [
        ('ACC', 'Accion'),
        ('COM', 'Comedia'),
        ('DRA', 'Drama'),
        ('TER', 'Terror'),
        ('SCI', 'Ciencia Ficcion'),
        ('ROM', 'Romance'),
        ('ANI', 'Animacion'),
        ('DOC', 'Documental'),
        ('OTH', 'Otro'),
    ]

    # Campos del modelo
    titulo = models.CharField(max_length=200, verbose_name="Título")
    descripcion = models.TextField(verbose_name="Descripción")
    año_lanzamiento = models.PositiveIntegerField(verbose_name="Año de Lanzamiento")
    genero = models.CharField(max_length=3, choices=GENERO_CHOICES, verbose_name="Género")
    duracion = models.PositiveIntegerField(verbose_name="Duración (en minutos)")
    director = models.CharField(max_length=100, verbose_name="Director")
    actores_principales = models.CharField(max_length=300, verbose_name="Actores Principales")
    calificacion = models.FloatField(verbose_name="Calificación (0-10)")
    imagen = models.ImageField(upload_to='peliculas/', verbose_name="Poster de la Película", null=True, blank=True)
    fecha_creacion = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de Creación")
    fecha_actualizacion = models.DateTimeField(auto_now=True, verbose_name="Fecha de Actualización")

    def __str__(self):
        return self.titulo  # Representación legible del modelo

    class Meta:
        verbose_name = "Película"
        verbose_name_plural = "Películas"
        ordering = ['-fecha_creacion']  # Ordenar por fecha de creación (más reciente primero)