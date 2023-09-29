from django.db import models
from django.contrib.auth.models import User
 
Lugar = [
    ("Aula","Aula"),
    ("Laboratorio","Laboratorio"),
]

class Hackaton(models.Model):
    Estudiante = models.ForeignKey(User, on_delete=models.CASCADE)
    Ciclo = models.CharField(max_length=25, default="Y23C2", blank=True)
    Conferencia = models.CharField(max_length=25, choices=Lugar)

    def __str__(self):
        return f'El Estudiante: {self.Estudiante} del ciclo {self.Ciclo}, asistio a la conferencia en el {self.Conferencia}'