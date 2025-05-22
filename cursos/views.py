from rest_framework import viewsets
from .models import Curso, Alumno
from .serializers import CursoSerializer, AlumnoSerializer
from usuarios.permissions import EsAdmin
from rest_framework.permissions import IsAuthenticated
from usuarios.permissions import EsCoordinador
from usuarios.permissions import EsAdminOCoordinador

class CursoViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated, EsAdminOCoordinador]
    queryset = Curso.objects.all()
    serializer_class = CursoSerializer

    def get_queryset(self):
        qs = super().get_queryset()
        if self.request.user.rol == 'coordinador':
            # sólo los cursos de su colegio
            return qs.filter(colegio__coordinador=self.request.user)
        return qs



class AlumnoViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated, EsCoordinador]
    queryset = Alumno.objects.all()
    serializer_class = AlumnoSerializer


    def get_queryset(self):
        curso_id = self.request.query_params.get('curso')
        if curso_id:
            return self.queryset.filter(curso_id=curso_id)
        return self.queryset.all()


from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from .models import Alumno
from .serializers import AlumnoSerializer

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def alumnos_por_colegio(request):
    colegio_id = request.GET.get('colegio')
    if not colegio_id:
        return Response([], status=400)
    alumnos = Alumno.objects.filter(colegio_id=colegio_id)
    serializer = AlumnoSerializer(alumnos, many=True)
    return Response(serializer.data)
