from rest_framework import viewsets
from escola.models import Curso
from escola.serializers import CursoSerializer



class CursosViewSet(viewsets.ModelViewSet):
    """Exibindo todos os cursos"""

    queryset = Curso.objects.all()
    serializer_class = CursoSerializer
