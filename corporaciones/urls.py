from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import CorporacionViewSet

router = DefaultRouter()
router.register(r'', CorporacionViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
