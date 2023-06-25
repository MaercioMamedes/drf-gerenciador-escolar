from rest_framework import viewsets
from escola.models import Curso
from escola.serializers import CursoSerializer
from escola.helpers import get_location



class CursosViewSet(viewsets.ModelViewSet):
    """Exibindo todos os cursos"""

    queryset = Curso.objects.all()
    serializer_class = CursoSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid(self):
            serializer.save()
            response = get_location(serializer, request)
            return response
