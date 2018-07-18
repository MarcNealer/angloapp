from django.contrib import admin

# Register your models here.
from .models import Grupo, Idioma, Nivel, Horario, Profesor, Salon, Alumno, Membership

admin.site.register(Grupo)
admin.site.register(Idioma)
admin.site.register(Nivel)
admin.site.register(Horario)
admin.site.register(Profesor)
admin.site.register(Salon)
admin.site.register(Alumno)
admin.site.register(Membership)


