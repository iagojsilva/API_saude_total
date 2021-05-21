from rest_framework import serializers
from core.models import Consulta
from core.validacoes import *

class ConsultaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Consulta
        fields = ['id','paciente', 'especialidade', 'profissional', 'data', 'horario_disponiveis']

class ListaPacienteConsultasSerializer(serializers.ModelSerializer):
    profissional = serializers.ReadOnlyField(source='profissional.nome')
    crm = serializers.ReadOnlyField(source='profissional.crm')
    especialidade = serializers.SerializerMethodField()
    
    class Meta:
        model = Consulta
        fields = ['id','profissional', 'especialidade', 'data', 'horario_disponiveis', 'crm']

    def get_especialidade(self, obj):
        return obj.profissional.especialidade.nome