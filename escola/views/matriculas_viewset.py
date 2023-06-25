from rest_framework import viewsets
from escola.models import Matricula
from escola.serializers import MatriculaSerializer

class MatriculaViewSet(viewsets.ModelViewSet):
    """Listando todas as matrículas"""
    
    queryset = Matricula.objects.all()
    serializer_class = MatriculaSerializer
