# backend/usuarios/views.py

from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from .models import Usuario
from .serializers import UsuarioSerializer
from .permissions import EsAdmin, EsCoordinador, EsContadora

from usuarios.permissions import EsAdminOCoordinador


class MeView(APIView):
    """
    Devuelve los datos del usuario autenticado.
    """
    permission_classes = [IsAuthenticated]

    def get(self, request):
        serializer = UsuarioSerializer(request.user)
        return Response(serializer.data)


class UsuarioViewSet(viewsets.ModelViewSet):
    """
    CRUD de usuarios completo. Solo accesible a Admin.
    """
    queryset = Usuario.objects.all()
    serializer_class = UsuarioSerializer
    permission_classes = [IsAuthenticated, EsAdmin]


class CoordinadorViewSet(viewsets.ModelViewSet):
    """
    CRUD de coordinadores. Solo accesible a Admin.
    """
    queryset = Usuario.objects.filter(rol='coordinador')
    serializer_class = UsuarioSerializer
    permission_classes = [IsAuthenticated, EsAdmin]


class ContadoraViewSet(viewsets.ModelViewSet):
    """
    CRUD de contadoras. Solo accesible a Admin.
    """
    queryset = Usuario.objects.filter(rol='contadora')
    serializer_class = UsuarioSerializer
    permission_classes = [IsAuthenticated, EsAdmin]



class ProfesorViewSet(viewsets.ReadOnlyModelViewSet):
    """
    Solo listar (y retrieve) los usuarios con rol='profesor'.
    Permitido a Admin y Coordinador.
    """
    queryset = Usuario.objects.filter(rol='profesor')
    serializer_class = UsuarioSerializer
    permission_classes = [IsAuthenticated, EsAdminOCoordinador]


from rest_framework.decorators import action


class UsuarioViewSet(viewsets.ModelViewSet):
    queryset = Usuario.objects.all()
    serializer_class = UsuarioSerializer
    permission_classes = [IsAuthenticated, EsAdmin]

    @action(detail=False, methods=['get'], url_path='profesores', permission_classes=[IsAuthenticated])
    def listar_profesores(self, request):
        profesores = Usuario.objects.filter(rol='profesor')
        serializer = self.get_serializer(profesores, many=True)
        return Response(serializer.data)
