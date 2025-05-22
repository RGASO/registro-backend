from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import CursoViewSet, AlumnoViewSet

router = DefaultRouter()
router.register(r'cursos', CursoViewSet)
router.register(r'alumnos', AlumnoViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
