# Generated by Django 5.0.6 on 2024-06-07 17:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Aspirante', '0005_carreras_clave_carreras_modalidad_capacidadatencion'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='capacidadatencion',
            name='idCarrera',
        ),
        migrations.RemoveField(
            model_name='carreras',
            name='idEmpleado',
        ),
    ]
