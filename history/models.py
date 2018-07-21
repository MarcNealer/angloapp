from django.db import models
# Create your models here.


class History(models.Model):
    nombre = models.CharField(max_length=100)
    fecha_inicio = models.DateField(null=True, blank=True)
    idioma = models.ForeignKey("grupos.Idioma", on_delete=models.SET_NULL, null=True)
    nivel = models.ForeignKey("grupos.Nivel", on_delete=models.SET_NULL, null=True)
    horario = models.ForeignKey("grupos.Horario", on_delete=models.SET_NULL, null=True)
    profesor = models.ForeignKey("grupos.Profesor", on_delete=models.SET_NULL, null=True)
    salon = models.ForeignKey("grupos.Salon", on_delete=models.SET_NULL, null=True)
    alumno = models.ForeignKey("grupos.Alumno", on_delete=models.SET_NULL, null=True)
    status = models.CharField(max_length=50)
    created = models.DateTimeField(editable=False, auto_now_add=True)

    def __str__(self):
        return self.nombre
