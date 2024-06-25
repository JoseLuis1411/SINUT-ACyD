from django.db import models

# Create your models here.

class dias(models.Model):
    idDia = models.AutoField(primary_key=True)
    dia = models.CharField(max_length=10)
    
class horarios(models.Model):
    idHorario = models.AutoField(primary_key=True)
    horario = models.CharField(max_length=15)

class Actividades(models.Model):
    idActividad = models.AutoField(primary_key=True)
    actividad = models.CharField(max_length=25)
    cupo = models.IntegerField()
    idMaestro = models.ForeignKey('Empleado.empleados', on_delete=models.CASCADE)
    idDia = models.ForeignKey('dias', on_delete=models.CASCADE)
    idHorario = models.ForeignKey('horarios', on_delete=models.CASCADE)