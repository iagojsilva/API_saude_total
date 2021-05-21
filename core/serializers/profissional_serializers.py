from rest_framework import serializers
from core.models import Profissional
from core.validacoes import *

class ProfissionalSerializer(serializers.ModelSerializer):
    especialidade = serializers.ReadOnlyField(source='especialidade.nome')
    data_disponiveis = serializers.SerializerMethodField()
    horario_disponiveis = serializers.SerializerMethodField()

    class Meta:
        model = Profissional
        fields = ['id','nome', 'especialidade', 'crm','horario_disponiveis', 'data_disponiveis']
    
    def get_data_disponiveis(self, obj):
        return obj.get_data_disponiveis_display()

    def get_horario_disponiveis(self, obj):
        return obj.get_horario_disponiveis_display()
        
    def validate(self, data):
        if not deve_ser_numero(data['crm']):
            raise ValidationError({'crm': 'Só é permitido números!'})
        
        if not deve_ser_string(data['nome']):
            raise ValidationError({'nome': 'Só é permitido caracteres alfabéticos!'})

        return data




class ListaProfissionaisEspecialidade(serializers.ModelSerializer):
    class Meta:
        model = Profissional
        fields = ['id']