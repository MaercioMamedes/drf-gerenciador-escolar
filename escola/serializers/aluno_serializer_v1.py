from rest_framework import serializers
from escola.models import Aluno

class AlunoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Aluno
        fields = ['id', 'nome', 'rg', 'cpf', 'data_nascimento']
        extra_kwargs = {'id': {'read_only': True}}
        