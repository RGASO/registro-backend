# backend/talleres/models.py
from django.db import models
from cursos.models import Curso, Alumno
from django.db import models
from django.conf import settings

class Taller(models.Model):
    nombre = models.CharField(max_length=100)
    curso = models.ForeignKey('cursos.Curso', on_delete=models.CASCADE, related_name='talleres')
    profesor = models.ForeignKey('usuarios.Usuario', on_delete=models.SET_NULL, null=True, blank=True)
    
    alumnos_asignados = models.ManyToManyField(Alumno, blank=True, related_name='talleres_asignados')

    def __str__(self):
        return f"{self.nombre}"
    
alumnos_asignados = models.ManyToManyField('cursos.Alumno', blank=True, related_name='talleres_asignados')
