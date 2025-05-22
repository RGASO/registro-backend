from django.db import models
from colegios.models import Colegio

class Curso(models.Model):
    nombre = models.CharField(max_length=50)
    colegio = models.ForeignKey(Colegio, on_delete=models.CASCADE, related_name='cursos')

    def __str__(self):
        return f'{self.nombre} - {self.colegio.nombre}'

class Alumno(models.Model):
    nombre = models.CharField(max_length=100)
    curso = models.ForeignKey(Curso, on_delete=models.CASCADE, related_name='alumnos')

    def __str__(self):
        return f'{self.nombre} - {self.curso.nombre}'
