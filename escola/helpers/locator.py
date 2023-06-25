from rest_framework.response import Response
from rest_framework import status


def get_location(serializer, request):
    """Método para gerar o location de um recurso novo criado"""
    
    response = Response(serializer.data, status=status.HTTP_201_CREATED)
    id_object = str(serializer.data['id'])
    response['location'] = request.build_absolute_uri() + id_object
    return response