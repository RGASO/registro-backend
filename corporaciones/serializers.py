# backend/corporaciones/serializers.py

from rest_framework import serializers
from usuarios.models import Usuario
from usuarios.serializers import UsuarioSerializer
from .models import Corporacion

class CorporacionSerializer(serializers.ModelSerializer):
    # lectura anidada
    coordinador = UsuarioSerializer(read_only=True)
    contadoras  = UsuarioSerializer(many=True, read_only=True)

    # escritura: mapeo de IDs
    coordinador_id = serializers.PrimaryKeyRelatedField(
        queryset=Usuario.objects.filter(rol='coordinador'),
        write_only=True,
        source='coordinador'
    )
    contadoras_ids = serializers.PrimaryKeyRelatedField(
        many=True,
        queryset=Usuario.objects.filter(rol='contadora'),
        write_only=True,
        source='contadoras'
    )

    class Meta:
        model = Corporacion
        fields = [
            'id',
            'nombre',
            'clave_adicional',
            'coordinador',     # para mostrar
            'contadoras',      # para mostrar
            'coordinador_id',  # para crear/editar
            'contadoras_ids',  # para crear/editar
        ]

    def create(self, validated_data):
        cont = validated_data.pop('contadoras', [])
        corp = Corporacion.objects.create(**validated_data)
        corp.contadoras.set(cont)
        return corp

    def update(self, instance, validated_data):
        cont = validated_data.pop('contadoras', None)
        for attr, val in validated_data.items():
            setattr(instance, attr, val)
        instance.save()
        if cont is not None:
            instance.contadoras.set(cont)
        return instance
