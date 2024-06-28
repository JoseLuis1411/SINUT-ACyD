from django.db import models

# Create your models here.
class periodo(models.Model):
    idPeriodo = models.AutoField(primary_key=True)
    fechaInicio = models.DateField()
    fechaFin = models.DateField()
    activo = models.IntegerField(null=True, blank=True)
    genTSU =models.IntegerField()
    genING =models.IntegerField()


class grupos(models.Model):
    idGrupo = models.AutoField(primary_key=True)
    grado = models.SmallIntegerField()
    grupo = models.CharField(max_length=1)
    turno = models.SmallIntegerField()
    idMaestro = models.ForeignKey('Empleado.empleados', on_delete=models.CASCADE)
    idCarrera = models.ForeignKey('Persona.carreras', on_delete=models.CASCADE)
    idPeriodo = models.ForeignKey('periodo', on_delete=models.CASCADE)

class estatusAlumnos(models.Model):
    idEstatusAlumno = models.AutoField(primary_key=True)
    nombreEstatus = models.CharField(max_length=50)

class alumnos(models.Model):
    id = models.AutoField(primary_key=True)
    matricula = models.CharField(max_length=10)
    nivel = models.SmallIntegerField() 
    fechaAlta = models.DateField()
    idEstatusAlumno = models.ForeignKey('estatusAlumnos', on_delete=models.CASCADE)
    idPersona=models.ForeignKey('Persona.personas', on_delete=models.CASCADE)
    idUsuarioInscribe = models.ForeignKey('Usuario.usuarios', on_delete=models.CASCADE)
    periodoInicio=models.ForeignKey('periodo', on_delete=models.CASCADE)
    
#models que me paso la maestra y yo puse en el proyecto
class gruposIngles(models.Model):
    idGrupoIngles = models.AutoField(primary_key=True)
    nivel = models.SmallIntegerField()
    idMaestro = models.ForeignKey('Empleado.empleados', on_delete=models.CASCADE)
    idPeriodo = models.ForeignKey('periodo', on_delete=models.CASCADE)
    descripcion = models.CharField(max_length=50)

class inscripciones(models.Model):
    idInscripcion = models.AutoField(primary_key=True)
    idAlumno = models.ForeignKey('alumnos', on_delete=models.CASCADE)
    idGrupo = models.ForeignKey('grupos', on_delete=models.CASCADE)
    IdGrupoIngles = models.ForeignKey('gruposIngles', on_delete=models.CASCADE)
    idActividadACyD = models.ForeignKey('ACyD.actividadesACyD', on_delete=models.CASCADE)
    idPeriodo = models.ForeignKey('periodo', on_delete=models.CASCADE)
    fechaInscripcion = models.DateField()
    idUsuarioInscribe = models.ForeignKey('Usuario.usuarios', on_delete=models.CASCADE)
    movimiento = models.SmallIntegerField()
    idPlanEstudios = models.SmallIntegerField()
      