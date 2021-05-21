from django.db import models
from multiselectfield import MultiSelectField
import datetime

class Especialidade(models.Model):
    nome = models.CharField(max_length=20, blank=False,)

    def __str__(self):
        return str(self.nome)

class Profissional(models.Model):
    HORARIOS = (
        ('T01', '13:30'), # T01 => Tarde 1
        ('M01', '09:30'), # M01 => Manha 1
        ('T02', '17:00'),
        ('T03', '19:00'),
        ('M02', '10:30'),
        ('M03', '07:00'),
    )

    DATAS = (
        ('D01', '2021-4-13'),
        ('D02', '2021-4-14'),
        ('D03', '2021-4-15'),
        ('D04', '2021-4-16'),
        ('D05', '2021-4-17'),
        ('D06', '2021-4-18'),
        ('D07', '2021-4-19')
    )

    nome = models.CharField(max_length=20, null=False, blank=False)
    horario_disponiveis = MultiSelectField(max_length=23, choices=HORARIOS, blank=False, min_choices=2, default=HORARIOS[0])
    data_disponiveis = MultiSelectField(max_length=23, choices=DATAS, blank=False, min_choices=2, default=DATAS[0])
    especialidade = models.ForeignKey(Especialidade, on_delete=models.CASCADE)
    crm = models.CharField(max_length=8)

    def __str__(self):
        return str(self.nome)

class Paciente(models.Model):
    nome = models.CharField(max_length=20, blank=False, default="Anonymus")

    def __str__(self):
        return str(self.nome)

class Consulta(models.Model):
    paciente = models.ForeignKey(Paciente, on_delete=models.CASCADE)
    especialidade = models.ForeignKey(Especialidade, on_delete=models.CASCADE)
    profissional = models.ForeignKey(Profissional, on_delete=models.CASCADE)
    data = models.DateField(max_length=19)
    horario_disponiveis = models.TimeField(max_length=5)

    def __str__(self):
        nome = self.profissional
        return f'consulta com {nome}'

