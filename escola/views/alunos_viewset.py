from rest_framework import viewsets
from rest_framework import filters
from escola.models import Aluno
from escola.serializers import AlunoSerializer
from escola.helpers import get_location
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404


class AlunosViewSet(viewsets.ModelViewSet):
    """métodos de acesso aos recursos da Classe Aluno"""

    # throttle_classes = [AnonRateThrottle]
    queryset = Aluno.objects.all()
    filter_backends = [filters.OrderingFilter, filters.SearchFilter] # customizar filtro
    ordering_fields = ['nome','id']
    search_fields = ['nome', 'cpf', 'rg']  # implementar método para tornar a busca mais otimizada
    serializer_class = AlunoSerializer    

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer_class()
        serializer = serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            response = get_location(serializer, request)
            return response
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def update(self, request, *args, **kwargs):
        aluno = get_object_or_404(Aluno, pk=kwargs['pk'])
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            serializer.update(aluno, serializer.validated_data)

            return Response(serializer.data, status=status.HTTP_200_OK)
        
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

 
    def partial_update(self, request, *args, **kwargs):
        print('passou')
        kwargs['partial'] = True
        return self.update(request, *args, **kwargs)