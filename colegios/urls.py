# backend/colegios/urls.py
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ColegioViewSet

router = DefaultRouter()
# especificamos basename porque ColegioViewSet no define .queryset a nivel de clase
router.register(r'', ColegioViewSet, basename='colegio')

urlpatterns = [
    path('', include(router.urls)),
]
