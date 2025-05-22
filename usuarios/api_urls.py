from rest_framework.routers import DefaultRouter
from .views import UsuarioViewSet, CoordinadorViewSet, ContadoraViewSet

router = DefaultRouter()
router.register(r'',             UsuarioViewSet,      basename='usuario')
router.register(r'coordinadores', CoordinadorViewSet, basename='coordinadores')
router.register(r'contadoras',    ContadoraViewSet,   basename='contadoras')

urlpatterns = router.urls
