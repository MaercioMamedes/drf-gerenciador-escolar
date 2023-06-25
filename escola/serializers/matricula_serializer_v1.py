from rest_framework import serializers
from escola.models import Matricula


class MatriculaSerializer(serializers.ModelSerializer):
    periodo = serializers.SerializerMethodField()
    class Meta:
        model = Matricula
        exclude = []

    def get_periodo(self, obj):
        return obj.get_periodo_display()