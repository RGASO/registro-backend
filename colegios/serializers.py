# backend/colegios/serializers.py

from rest_framework import serializers
from usuarios.models import Usuario
from usuarios.serializers import UsuarioSerializer
from .models import Colegio

class ColegioSerializer(serializers.ModelSerializer):
    # lectura anidada
    corporacion = serializers.StringRelatedField()
    coordinador  = UsuarioSerializer(read_only=True)

    # escritura
    corporacion_id = serializers.PrimaryKeyRelatedField(
        queryset=   Colegio._meta.get_field('corporacion').related_model.objects.all(),
        source=     'corporacion',
        write_only= True
    )
    coordinador_id = serializers.PrimaryKeyRelatedField(
        queryset=   Usuario.objects.filter(rol='coordinador'),
        source=     'coordinador',
        write_only= True,
        allow_null=True
    )

    class Meta:
        model  = Colegio
        fields = [
            'id',
            'nombre',
            'corporacion',    # para mostrar
            'coordinador',    # para mostrar
            'corporacion_id', # para crear/editar
            'coordinador_id'  # para crear/editar
        ]
