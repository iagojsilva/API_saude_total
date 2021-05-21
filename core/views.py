from django.shortcuts import render
from rest_framework import viewsets, generics
from .models import Consulta, Profissional, Paciente, Especialidade
from .serializer import ConsultaSerializer, ProfissionalSerializer, PacienteSerializer, EspecialidadeSerializer, ListaPacienteConsultasSerializer, ListaProfissionaisEspecialidade

class EspecialidadeViewSet(viewsets.ModelViewSet):
    """Listando todas as especialidades"""
    queryset = Especialidade.objects.all()
    serializer_class = EspecialidadeSerializer

class ConsultaViewSet(viewsets.ModelViewSet):
    """Listando todas as consulta marcadas"""
    queryset = Consulta.objects.all()
    serializer_class = ConsultaSerializer

class ProfissionalViewSet(viewsets.ModelViewSet):
    """Listando todos os profissionais"""
    queryset = Profissional.objects.all()
    serializer_class = ProfissionalSerializer

class PacienteViewSet(viewsets.ModelViewSet):
    queryset = Paciente.objects.all()
    serializer_class = PacienteSerializer

class ListaConsultasPaciente(generics.ListAPIView):
    """Listando consultas de um determinado Paciente"""

    def get_queryset(self):
        queryset = Consulta.objects.filter(paciente_id=self.kwargs['pk'])
        return queryset

    serializer_class = ListaPacienteConsultasSerializer

class ListaProfissionaisEspecialidade(generics.ListAPIView):
    """Listando profissionais de acordo com a especialidade"""

    def get_queryset(self):
        queryset = Profissional.objects.filter(especialidade_id=self.kwargs['pk'])
        return queryset

    serializer_class = ListaProfissionaisEspecialidade