from rest_framework import serializers
from escola.models import Aluno
from escola.helpers import nome_valido ,cpf_valido, rg_valido

class AlunoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Aluno
        fields = ['id', 'nome', 'rg', 'cpf', 'data_nascimento']
        extra_kwargs = {'id': {'read_only': True}}

    def validate(self, attrs):
        lista_erros = {}
        print('passou')
        if not nome_valido(attrs['nome']):
            lista_erros['nome'] = 'O campo nome não pode conter caracteres numéricos ou especiais'
    
        if not rg_valido(attrs['rg']):
            lista_erros['rg'] = 'rg inválido'
        
        if not cpf_valido(attrs['cpf']):
            lista_erros['cpf'] = 'CPF inválido'
        
        if lista_erros:
            raise serializers.ValidationError(lista_erros)
  
        return attrs
        