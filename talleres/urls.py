# backend/talleres/urls.py
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import TallerViewSet
from .views import TallerProfesorViewSet

router = DefaultRouter()
router.register(r'talleres', TallerViewSet)
router.register(r'mis-talleres', TallerProfesorViewSet, basename='mis-talleres')
router.register(r'profesor/talleres', TallerProfesorViewSet, basename='talleres-profesor')

urlpatterns = [
    path('', include(router.urls)),
]

