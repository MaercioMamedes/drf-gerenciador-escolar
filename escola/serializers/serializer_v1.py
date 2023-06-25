from rest_framework import serializers
from escola.models import Aluno, Curso, Matricula

class AlunoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Aluno
        fields = ['id', 'nome', 'rg', 'cpf', 'data_nascimento']
        extra_kwargs = {'id': {'read_only': True}}

class CursoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Curso
        fields = '__all__'

class MatriculaSerializer(serializers.ModelSerializer):
    periodo = serializers.SerializerMethodField()
    class Meta:
        model = Matricula
        exclude = []

    def get_periodo(self, obj):
        return obj.get_periodo_display()

class ListaMatriculasAlunoSerializer(serializers.ModelSerializer):
    curso_id = serializers.ReadOnlyField(source='curso.id')
    curso = serializers.ReadOnlyField(source='curso.descricao')
    periodo = serializers.SerializerMethodField()
    class Meta:
        model = Matricula
        fields = ['curso_id','curso', 'periodo']
    def get_periodo(self, obj):
        return obj.get_periodo_display()

class ListaAlunosMatriculadosSerializer(serializers.ModelSerializer):
    aluno_id = serializers.ReadOnlyField(source='aluno.id')
    aluno_nome = serializers.ReadOnlyField(source='aluno.nome')
    class Meta:
        model = Matricula
        fields = ['aluno_id', 'aluno_nome']