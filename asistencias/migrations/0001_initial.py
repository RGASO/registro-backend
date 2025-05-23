# Generated by Django 5.2.1 on 2025-05-07 20:25

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('cursos', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Asistencia',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha', models.DateField()),
                ('alumnos_presentes', models.ManyToManyField(related_name='asistencias', to='cursos.alumno')),
            ],
        ),
    ]
