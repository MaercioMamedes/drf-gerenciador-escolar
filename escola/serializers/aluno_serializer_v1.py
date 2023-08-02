from rest_framework import serializers
from escola.models import Aluno
from escola.helpers import nome_valido,cpf_valido, rg_valido, celular_valido


class AlunoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Aluno
        fields = ['id', 'nome', 'rg', 'cpf', 'data_nascimento', 'celular','foto']
        extra_kwargs = {
            'id': {'read_only': True},
            'foto': {'read_only': True},
            }

    def validate(self, attrs):
        lista_erros = {}

        if ('nome' in attrs) and not nome_valido(attrs['nome']):
            lista_erros['nome'] = 'O campo nome não pode conter caracteres numéricos ou especiais'
    
        if ('rg' in attrs) and not rg_valido(attrs['rg']):
            lista_erros['rg'] = 'RG inválido'
        
        if ('cpf' in attrs) and not cpf_valido(attrs['cpf']):
            lista_erros['cpf'] = 'CPF inválido'
        
        if ('celular' in attrs) and not celular_valido(attrs['celular']):
            lista_erros['celular'] = 'formato do número do celular inválido'

        if lista_erros:

            raise serializers.ValidationError(lista_erros)
        else:

            return attrs
        