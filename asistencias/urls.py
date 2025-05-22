# backend/asistencias/urls.py
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import AsistenciaViewSet, HistorialAsistenciaViewSet, EstadisticasViewSet

router = DefaultRouter()
router.register(r'', AsistenciaViewSet, basename='asistencias')
router.register(r'historial', HistorialAsistenciaViewSet)
router.register(r'estadisticas', EstadisticasViewSet, basename='estadisticas')

urlpatterns = [
    path('', include(router.urls)),
]
