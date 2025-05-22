from rest_framework import serializers
from .models import Taller
from cursos.models import Alumno
from django.contrib.auth import get_user_model

Usuario = get_user_model()

class AlumnoLiteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Alumno
        fields = ['id', 'nombre']

class TallerSerializer(serializers.ModelSerializer):
    profesor = serializers.PrimaryKeyRelatedField(
        queryset=Usuario.objects.filter(rol='profesor'),
        allow_null=True,
        required=False
    )
    profesor_username = serializers.CharField(source='profesor.username', read_only=True)

    # 🔽 usamos uno para escritura y otro para lectura
    alumnos_asignados = AlumnoLiteSerializer(many=True, read_only=True)
    alumnos_asignados_ids = serializers.PrimaryKeyRelatedField(
        source='alumnos_asignados',
        many=True,
        queryset=Alumno.objects.all(),
        write_only=True
    )

    class Meta:
        model = Taller
        fields = [
            'id', 'nombre', 'curso', 'profesor', 'profesor_username',
            'alumnos_asignados', 'alumnos_asignados_ids'
        ]
