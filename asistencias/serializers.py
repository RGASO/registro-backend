from rest_framework import serializers
from .models import Asistencia, HistorialAsistencia


class AsistenciaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Asistencia
        fields = '__all__'
        extra_kwargs = {
            'profesor': {'required': False}
        }

class HistorialAsistenciaSerializer(serializers.ModelSerializer):
    class Meta:
        model = HistorialAsistencia
        fields = '__all__'
