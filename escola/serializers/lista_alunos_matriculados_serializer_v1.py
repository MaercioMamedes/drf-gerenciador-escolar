from rest_framework import serializers
from escola.models import Matricula


class ListaAlunosMatriculadosSerializer(serializers.ModelSerializer):
    aluno_id = serializers.ReadOnlyField(source='aluno.id')
    aluno_nome = serializers.ReadOnlyField(source='aluno.nome')
    class Meta:
        model = Matricula
        fields = ['aluno_id', 'aluno_nome']