from rest_framework import viewsets
from escola.models import Matricula
from escola.serializers import MatriculaSerializer
from escola.helpers import get_location

class MatriculaViewSet(viewsets.ModelViewSet):
    """Listando todas as matrículas"""
    
    queryset = Matricula.objects.all()
    serializer_class = MatriculaSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid(self):
            serializer.save()
            response = get_location(serializer, request)
            return response