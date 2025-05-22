# backend/usuarios/urls.py
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import (
    UsuarioViewSet,
    CoordinadorViewSet,
    ContadoraViewSet,
    ProfesorViewSet,
)

router = DefaultRouter()
router.register(r'coordinadores', CoordinadorViewSet, basename='coordinadores')
router.register(r'contadoras', ContadoraViewSet, basename='contadoras')
router.register(r'profesores', ProfesorViewSet, basename='profesores')
router.register(r'', UsuarioViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
