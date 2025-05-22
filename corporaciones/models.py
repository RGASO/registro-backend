from django.db import models
from django.conf import settings

class Corporacion(models.Model):
    nombre = models.CharField(max_length=100)
    rut = models.CharField(max_length=12, unique=True, blank=True, null=True)
    clave_adicional = models.CharField(max_length=50, blank=True)

    coordinador = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        limit_choices_to={'rol': 'coordinador'},
        related_name='coordinador_de'
    )
    contadoras = models.ManyToManyField(
        settings.AUTH_USER_MODEL,
        blank=True,
        limit_choices_to={'rol': 'contadora'},
        related_name='contadora_de'
    )

    usuario = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='corporacion',
        null=True,  # 👈 AGREGAS ESTO
        blank=True  # 👈 Y ESTO
    )


    def __str__(self):
        return self.nombre

    def __str__(self):
        return self.nombre
