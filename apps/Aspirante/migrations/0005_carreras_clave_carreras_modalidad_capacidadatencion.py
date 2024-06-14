# Generated by Django 5.0.6 on 2024-06-06 20:21

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Aspirante', '0004_carreras_idempleado'),
    ]

    operations = [
        migrations.AddField(
            model_name='carreras',
            name='clave',
            field=models.CharField(default=4081100009, max_length=10),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='carreras',
            name='modalidad',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
        migrations.CreateModel(
            name='capacidadAtencion',
            fields=[
                ('idCapacidad', models.AutoField(primary_key=True, serialize=False)),
                ('capacidadAtencion', models.IntegerField()),
                ('proyeccionFichas', models.IntegerField()),
                ('ciclo', models.CharField(max_length=9)),
                ('idCarrera', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Aspirante.carreras')),
            ],
        ),
    ]
