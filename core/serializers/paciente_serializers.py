from rest_framework import serializers
from core.models import Paciente
from core.validacoes import *

class PacienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Paciente
        exclude = []


