# Generated by Django 2.0.7 on 2018-07-18 06:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('grupos', '__first__'),
    ]

    operations = [
        migrations.CreateModel(
            name='History',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100, unique=True)),
                ('fecha_inicio', models.DateField(blank=True, null=True)),
                ('status', models.CharField(max_length=50)),
                ('alumno', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='grupos.Alumno')),
                ('horario', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='grupos.Horario')),
                ('idioma', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='grupos.Idioma')),
                ('nivel', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='grupos.Nivel')),
                ('profesor', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='grupos.Profesor')),
                ('salon', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='grupos.Salon')),
            ],
        ),
    ]
