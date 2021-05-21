from django.contrib import admin
from .models import Consulta, Profissional, Paciente, Especialidade

admin.site.register(Consulta)
admin.site.register(Profissional)
admin.site.register(Paciente)
admin.site.register(Especialidade)


# Register your models here.
