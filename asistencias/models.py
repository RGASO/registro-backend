from django.db import models
from talleres.models import Taller
from cursos.models import Alumno
from usuarios.models import Usuario

class Asistencia(models.Model):
    taller = models.ForeignKey(Taller, on_delete=models.CASCADE, related_name='asistencias')
    fecha = models.DateField()
    profesor = models.ForeignKey(Usuario, on_delete=models.CASCADE, limit_choices_to={'rol': 'profesor'})
    alumnos_presentes = models.ManyToManyField(Alumno, related_name='asistencias')

    def __str__(self):
        return f'{self.taller.nombre} - {self.fecha}'


class HistorialAsistencia(models.Model):
    alumno = models.ForeignKey(Alumno, on_delete=models.CASCADE)
    taller = models.ForeignKey(Taller, on_delete=models.CASCADE)
    fecha = models.DateField()
    presente = models.BooleanField()

    def __str__(self):
        return f'{self.alumno.nombre} - {self.fecha} - {"Presente" if self.presente else "Ausente"}'
