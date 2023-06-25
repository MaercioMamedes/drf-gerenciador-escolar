from rest_framework.serializers import ModelSerializer
from escola.models import Aluno


class AlunoSerializerV2(ModelSerializer):
    class Meta:
        model = Aluno
        fields = '__all__'
