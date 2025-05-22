from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from usuarios.permissions import EsAdminOCoordinador, EsAdminOCliente
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import OrderingFilter
from .models import Colegio
from .serializers import ColegioSerializer

class ColegioViewSet(viewsets.ModelViewSet):
    serializer_class = ColegioSerializer
    permission_classes = [IsAuthenticated]
    filter_backends = [DjangoFilterBackend, OrderingFilter]
    filterset_fields = ['corporacion']
    ordering_fields  = ['nombre', 'corporacion__nombre']
    ordering         = ['corporacion__nombre', 'nombre']

    def get_queryset(self):
        user = self.request.user

        if user.rol == 'coordinador':
            return Colegio.objects.filter(coordinador=user)

        if user.rol == 'cliente':  # cliente = corporación
            return Colegio.objects.filter(corporacion__usuario=user)

        return Colegio.objects.all()
