"""api URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from rest_framework import routers

from core.views import ConsultaViewSet, ProfissionalViewSet, PacienteViewSet, EspecialidadeViewSet, ListaConsultasPaciente, ListaProfissionaisEspecialidade

router = routers.DefaultRouter()

router.register(r'consultas', ConsultaViewSet, basename="Consultas")
router.register(r'profissional', ProfissionalViewSet, basename="Profissionais")
router.register(r'paciente', PacienteViewSet, basename="Pacientes")
router.register(r'especialidade', EspecialidadeViewSet, basename="Especialidades")


urlpatterns = [
    path('paciente/<int:pk>/consultas/', ListaConsultasPaciente.as_view()),
    path('especialidade/<int:pk>/profissionais/', ListaProfissionaisEspecialidade.as_view()),
    path('', include(router.urls)),
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls'))
]
