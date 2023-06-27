from rest_framework import serializers
from escola.models import Aluno
from escola.helpers import nome_valido ,cpf_valido, rg_valido, celular_valido


class AlunoSerializerV2(serializers.ModelSerializer):
    class Meta:
        model = Aluno
        fields = '__all__'
        fields = ['id', 'nome', 'rg', 'cpf', 'data_nascimento', 'celular']
        extra_kwargs = {'id': {'read_only': True}}

    def validate(self, attrs):
        lista_erros = {}

        if not nome_valido(attrs['nome']):
            lista_erros['nome'] = 'O campo nome não pode conter caracteres numéricos ou especiais'
    
        if not rg_valido(attrs['rg']):
            lista_erros['rg'] = 'RG inválido'
        
        if not cpf_valido(attrs['cpf']):
            lista_erros['cpf'] = 'CPF inválido'
        
        if not celular_valido(attrs['celular']):
            lista_erros['celular'] = 'formato do número do celular inválido'
        
        

        if not lista_erros:
            print('asdas')
            return attrs
        else:
            # print(lista_erros)
            raise serializers.ValidationError(lista_erros)