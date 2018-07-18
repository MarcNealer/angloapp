from django.contrib import admin

# Register your models here.
from .models import  Prospecto, Idioma, Horario, Accion, Razon

# admin.site.register(Prospecto)
admin.site.register(Idioma)
admin.site.register(Horario)
admin.site.register(Accion)
admin.site.register(Razon)

# Define the admin class
class ProspectoAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'apaterno', 'amaterno', 'cel', 'tel', 'email', 'idioma', 'horario', 'comentario', 'pub_date')

# Register the admin class with the associated model
admin.site.register(Prospecto, ProspectoAdmin)