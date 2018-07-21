from django.db import models
from django.core.exceptions import ValidationError
from django.urls import reverse #Used to generate URLs by reversing the URL patterns
from django.contrib.auth.models import User #Autor de la "acción" en prospecto
from datetime import date #creo que no es necesario para DateField
from django.db.models.signals import post_save
from .db_signal import save_history

class Idioma(models.Model):
    """
    Model representing a language (French, spanish, etc).
    """
    name = models.CharField(max_length=100, help_text="Ingresa el idioma de interés (Inglés, Español etc.)")

    def __str__(self):
        """
        String for representing the Model object (in Admin site etc.)
        """
        return self.name
        
class Nivel(models.Model):
    """
    Model representing a the level (Start 1, Start 2, Start 3, etc).
    """
    idioma = models.ForeignKey(Idioma, on_delete=models.CASCADE, null=True)
    name = models.CharField(max_length=100, help_text="Ingresa el nivel)")
    

    def __str__(self):
        """
        String for representing the Model object (in Admin site etc.)
        """
        return self.name
        
class Grupo(models.Model):
    """
    Model representing a classroom group
    """
    nombre = models.CharField(max_length=100, unique=True)
    fecha_inicio = models.DateField(null=True, blank=True)
    idioma = models.ForeignKey(Idioma, on_delete=models.SET_NULL, null=True)
    nivel = models.ForeignKey(Nivel, on_delete=models.SET_NULL, null=True)
    horario = models.ForeignKey('Horario', on_delete=models.SET_NULL, null=True)
    profesor = models.ForeignKey('Profesor', on_delete=models.SET_NULL, null=True)
    salon = models.ForeignKey('Salon', on_delete=models.SET_NULL, null=True)
    members = models.ManyToManyField('Alumno',related_name='preubanormal', through='Membership')
    
    def get_absolute_url(self):
        """
        Returns the url to access a particular author instance.
        """
        return reverse('grupo-detail', kwargs={'pk': self.pk})
    
    def __str__(self):
        """
        String for representing the Model object.
        """
        return self.nombre
                
class Horario(models.Model):
    """
    Modelo representando un horario (7:840, 9-11am, etc).
    """
    name = models.CharField(max_length=100, help_text="Ingresa el horario")

    def __str__(self):
        """
        String for representing the Model object (in Admin site etc.)
        """
        return self.name
        
class Profesor(models.Model):
    """
    Modelo representando un profesor (Juan, Lulu, Antonio, etc).
    """
    name = models.CharField(max_length=100, help_text="Ingresa el profesor")

    def __str__(self):
        """
        String for representing the Model object (in Admin site etc.)
        """
        return self.name
        
class Salon(models.Model):
    """
    Modelo representando un aula (Aula 1, Aula 2, Aula 3).
    """
    name = models.CharField(max_length=100, help_text="Ingresa el aula")

    def __str__(self):
        """
        String for representing the Model object (in Admin site etc.)
        """
        return self.name
        
class Alumno(models.Model):
    """
    Model representing a student
    """
    nombre = models.CharField(max_length=100)
    apaterno = models.CharField(max_length=100)
    amaterno = models.CharField(max_length=100, blank=True, null=True)
    cel = models.IntegerField(blank=True, null=True)
    tel = models.IntegerField(blank=True, null=True)
    email = models.EmailField(blank=True, null=True)
    fecha_nacimiento = models.DateField(null=True, blank=True)
    direccion = models.CharField(max_length=400)

    def clean(self):
        if not (self.cel or self.tel or self.email):
            raise ValidationError("Debes de agregar almenos un dato de contacto (cel, tel o email)")

    def get_absolute_url(self):
        """
        Returns the url to access a particular author instance.
        """
        return reverse('alumno-detail', kwargs={'pk': self.pk})


    def __str__(self):
        """
        String for representing the Model object.
        """
        return self.nombre + ' ' + self.apaterno

class Membership(models.Model):

    STATUS = (
        ('i', 'Inscrito'),
        ('p', 'Pre-inscrito'),
    )

    alumno = models.ForeignKey(Alumno, on_delete=models.CASCADE)
    grupo = models.ForeignKey(Grupo, on_delete=models.CASCADE, null=True)
    status = models.CharField(max_length=1, choices=STATUS, blank=True, default='p')
    
    def get_absolute_url(self):
        """
        Returns the url to access a particular author instance.
        """
        return reverse('grupo-detail', kwargs={'pk': self.grupo.id})

post_save.connect(save_history, sender=Membership)
