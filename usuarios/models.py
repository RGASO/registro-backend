from django.contrib.auth.models import AbstractUser
from django.db import models

ROLES = (
    ('admin', 'Administradora'),
    ('profesor', 'Profesor'),
    ('coordinador', 'Coordinador'),
    ('cliente', 'Cliente'),
    ('contadora', 'Contadora'),
)

class Usuario(AbstractUser):
    rol = models.CharField(max_length=20, choices=ROLES)
