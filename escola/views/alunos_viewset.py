from rest_framework import viewsets
from rest_framework import filters
from escola.models import Aluno
from escola.serializers import AlunoSerializer
from escola.helpers import get_location
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404
import os


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
            if not serializer.validated_data['foto']:
                serializer.validated_data['foto'] = aluno.foto
                instance = self.get_object()
                serializer.update(instance, serializer.validated_data)
                serializer = self.get_serializer(instance)
                return Response(serializer.data, status=status.HTTP_200_OK)

            else:
                instance = self.get_object()
                instance.foto.delete(save=False)
                serializer.update(instance, serializer.validated_data)
                serializer = self.get_serializer(instance)
                return Response(serializer.data, status=status.HTTP_200_OK)
        
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def partial_update(self, request, *args, **kwargs):
        aluno = get_object_or_404(Aluno, pk=kwargs['pk'])
        serializer = self.get_serializer(data=request.data, partial=True)
        if serializer.is_valid():
            if 'foto' not in serializer.validated_data:
                instance = self.get_object()
                serializer.update(instance, serializer.validated_data)
                serializer = self.get_serializer(instance)
                return Response(serializer.data, status=status.HTTP_200_OK)

            elif serializer.validated_data['foto'] is not None:
                instance = self.get_object()
                instance.foto.delete(save=False)
                serializer.update(instance, serializer.validated_data)
                serializer = self.get_serializer(instance)
                return Response(serializer.data, status=status.HTTP_200_OK)

            else:
                serializer.validated_data['foto'] = aluno.foto
                instance = self.get_object()
                serializer.update(instance, serializer.validated_data)
                serializer = self.get_serializer(instance)
                return Response(serializer.data, status=status.HTTP_200_OK)

        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.delete()
        return Response('objeto deletado', status=status.HTTP_200_OK)
