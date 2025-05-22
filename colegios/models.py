# backend/colegios/models.py

from django.db import models
from django.conf import settings
from corporaciones.models import Corporacion
from django.conf import settings

class Colegio(models.Model):
    nombre = models.CharField(max_length=100)
    corporacion = models.ForeignKey(
        Corporacion,
        on_delete=models.CASCADE,
        related_name='colegios'
    )

    # Nuevo: cada colegio tiene un coordinador
    coordinador = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        limit_choices_to={'rol': 'coordinador'},
        related_name='colegio_asignado'
    )

    def __str__(self):
        return self.nombre
