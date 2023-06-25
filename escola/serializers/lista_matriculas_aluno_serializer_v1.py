from rest_framework import serializers
from escola.models import Matricula


class ListaMatriculasAlunoSerializer(serializers.ModelSerializer):
    curso_id = serializers.ReadOnlyField(source='curso.id')
    curso = serializers.ReadOnlyField(source='curso.descricao')
    periodo = serializers.SerializerMethodField()
    class Meta:
        model = Matricula
        fields = ['curso_id','curso', 'periodo']
    def get_periodo(self, obj):
        return obj.get_periodo_display()