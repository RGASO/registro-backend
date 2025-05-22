from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from usuarios.permissions import EsAdmin
from .models import Corporacion
from .serializers import CorporacionSerializer

class CorporacionViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated, EsAdmin]
    queryset = Corporacion.objects.all()
    serializer_class = CorporacionSerializer
