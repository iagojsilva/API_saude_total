from rest_framework import serializers
from core.models import Especialidade
from core.validacoes import *

class EspecialidadeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Especialidade
        fields = ['id','nome']

    def validate(self, data):
        if not deve_ser_string(data['nome']):
            raise serializers.ValidationError({'nome': 'Só é permitido caracteres alfabéticos!'})
    
        return data