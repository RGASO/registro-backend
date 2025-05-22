# backend/talleres/views.py
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from usuarios.permissions import EsAdminOCoordinador
from .models import Taller
from .serializers import TallerSerializer
from usuarios.permissions import EsProfesor

class TallerViewSet(viewsets.ModelViewSet):
    queryset = Taller.objects.all()
    serializer_class = TallerSerializer
    permission_classes = [IsAuthenticated, EsAdminOCoordinador]

    def get_queryset(self):
        qs = super().get_queryset()
        user = self.request.user

        if user.rol == 'coordinador':
            qs = qs.filter(curso__colegio__coordinador=user)

        curso_id = self.request.query_params.get('curso')
        if curso_id:
            qs = qs.filter(curso_id=curso_id)

        return qs
    
    def partial_update(self, request, *args, **kwargs):
        return super().partial_update(request, *args, **kwargs)


class TallerProfesorViewSet(viewsets.ReadOnlyModelViewSet):
    """
    Lista los talleres asignados al profesor autenticado.
    """
    permission_classes = [IsAuthenticated, EsProfesor]
    serializer_class = TallerSerializer

    def get_queryset(self):
        return Taller.objects.filter(profesor=self.request.user)
