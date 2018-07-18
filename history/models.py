from django.db import models
from grupos.models import Idioma, Nivel, Salon, Horario, Profesor, Alumno
# Create your models here.


class History(models.Model):
    nombre = models.CharField(max_length=100, unique=True)
    fecha_inicio = models.DateField(null=True, blank=True)
    idioma = models.ForeignKey(Idioma, on_delete=models.SET_NULL, null=True)
    nivel = models.ForeignKey(Nivel, on_delete=models.SET_NULL, null=True)
    horario = models.ForeignKey(Horario, on_delete=models.SET_NULL, null=True)
    profesor = models.ForeignKey(Profesor, on_delete=models.SET_NULL, null=True)
    salon = models.ForeignKey(Salon, on_delete=models.SET_NULL, null=True)
    alumno = models.ForeignKey(Alumno, on_delete=models.SET_NULL, null=True)
    status = models.CharField(max_length=50)
    created = models.DateTimeField(editable=False, auto_now_add=True)

    def __str__(self):
        return self.nombre
