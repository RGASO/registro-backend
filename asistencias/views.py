from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from django.db.models import Count
from datetime import datetime, date
import calendar

from .models import Asistencia, HistorialAsistencia
from .serializers import AsistenciaSerializer, HistorialAsistenciaSerializer
from talleres.models import Taller
from cursos.models import Alumno

from usuarios.permissions import EsAdminOCliente, EsProfesor, EsContadora

class AsistenciaViewSet(viewsets.ModelViewSet):
    """
    CRUD de asistencias. Solo los profesores pueden crear.
    """
    queryset = Asistencia.objects.all()
    serializer_class = AsistenciaSerializer

    def get_permissions(self):
        if self.action == 'create':
            return [IsAuthenticated(), EsProfesor()]
        return [IsAuthenticated()]

    def create(self, request, *args, **kwargs):
        # El profesor se asigna automáticamente
        data = request.data.copy()
        data['profesor'] = request.user.id
        serializer = self.get_serializer(data=data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        return Response(serializer.data)

    def perform_create(self, serializer):
        serializer.save()


class HistorialAsistenciaViewSet(viewsets.ModelViewSet):
    """CRUD de historial de asistencias (cualquier usuario autenticado)."""
    permission_classes = [IsAuthenticated]
    queryset = HistorialAsistencia.objects.all()
    serializer_class = HistorialAsistenciaSerializer

class EstadisticasViewSet(viewsets.ViewSet):
    """
    Estadísticas generales:
      - GET /api/asistencias/estadisticas/por_taller/
      - GET /api/asistencias/estadisticas/informe/mensual/
    Solo admin, cliente o contadora.
    """
    permission_classes = [IsAuthenticated, EsAdminOCliente | EsContadora]

    @action(detail=False, methods=['get'], url_path='informe/mensual')
    def informe_mensual(self, request):
        colegio_id = request.query_params.get('colegio')
        mes        = request.query_params.get('mes')
        año        = request.query_params.get('año')

        if not (colegio_id and mes and año):
            return Response(
                {'error': 'Faltan parámetros: colegio, mes o año'},
                status=400
            )

        year  = int(año)
        month = int(mes)
        start = date(year, month, 1)
        end   = date(year, month, calendar.monthrange(year, month)[1])

        talleres = Taller.objects.filter(curso__colegio_id=colegio_id)
        data = []
        for t in talleres:
            asistencias = t.asistencias.filter(fecha__range=(start, end))
            total_clases   = asistencias.count()
            total_alumnos  = Alumno.objects.filter(curso=t.curso).count()
            total_presentes = sum(a.alumnos_presentes.count() for a in asistencias)

            promedio = (
                round((total_presentes / (total_alumnos * total_clases)) * 100, 2)
                if total_clases and total_alumnos else 0
            )

            data.append({
                'colegio': t.curso.colegio.nombre,
                'curso':   t.curso.nombre,
                'taller':  t.nombre,
                'promedio_asistencia': promedio,
                'mes': f'{year}-{month:02}',
            })

        return Response(data)

    @action(
        detail=False,
        methods=['get'],
        url_path='por_taller',
        permission_classes=[IsAuthenticated, EsAdminOCliente | EsContadora]
    )
    def estadisticas_por_taller(self, request):
        colegio_id   = request.query_params.get('colegio')
        fecha_inicio = request.query_params.get('fecha_inicio')
        fecha_fin    = request.query_params.get('fecha_fin')

        if not colegio_id:
            return Response({'error': 'Falta parámetro colegio'}, status=400)

        asistencias = Asistencia.objects.filter(taller__curso__colegio_id=colegio_id)

        if fecha_inicio and fecha_fin:
            asistencias = asistencias.filter(
                fecha__range=[fecha_inicio, fecha_fin]
            )

        stats = (
            asistencias.values(
                'taller__nombre', 'taller__curso__nombre', 'taller__curso__colegio__nombre'
            ).annotate(
                total_clases=Count('id'),
                total_asistencias=Count('alumnos_presentes')
            )
        )

        resultado = [
            {
                'colegio': s['taller__curso__colegio__nombre'],
                'curso': s['taller__curso__nombre'],
                'taller': s['taller__nombre'],
                'promedio_asistencia': round(
                    (s['total_asistencias'] / s['total_clases']) * 100, 2
                ) if s['total_clases'] else 0
            }
            for s in stats
        ]

        return Response(resultado)
