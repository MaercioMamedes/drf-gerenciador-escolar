from rest_framework import serializers
from escola.models import Aluno
from escola.helpers import nome_valido ,cpf_valido, rg_valido, celular_valido

class AlunoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Aluno
        fields = ['id', 'nome', 'rg', 'cpf', 'data_nascimento']
        extra_kwargs = {'id': {'read_only': True}}

    def validate(self, attrs):

        return attrs
        