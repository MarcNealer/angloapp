from django.db import models
from django.core.exceptions import ValidationError
from django.urls import reverse #Used to generate URLs by reversing the URL patterns
from django.contrib.auth.models import User #Autor de la "acción" en prospecto

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

class Prospecto(models.Model):
    """
    Model representing a prospect
    """
    STATUS = (
        ('p', 'Prospecto Activo'),
        ('d', 'Desinteresado'),
    )
    
    status = models.CharField(max_length=1, choices=STATUS, blank=True, default='p', help_text='Status del prospecto')
    nombre = models.CharField(max_length=100)
    apaterno = models.CharField(max_length=100)
    amaterno = models.CharField(max_length=100, blank=True, null=True)
    cel = models.IntegerField(blank=True, null=True)
    tel = models.IntegerField(blank=True, null=True)
    email = models.EmailField(blank=True, null=True)
    idioma = models.ForeignKey(Idioma, on_delete=models.SET_NULL, null=True)
    horario = models.ForeignKey('Horario', on_delete=models.SET_NULL, null=True)
    comentario = models.TextField(max_length=2000, help_text='Agrega una nota u comentario')
    pub_date = models.DateField(auto_now_add=True)

    def clean(self):
        if not (self.cel or self.tel or self.email):
            raise ValidationError("Debes de agregar almenos un dato de contacto (cel, tel o email)")

    def get_absolute_url(self):
        """
        Returns the url to access a particular author instance.
        """
        return reverse('prospecto-detail', kwargs={'pk': self.pk})


    def __str__(self):
        """
        String for representing the Model object.
        """
        return self.nombre


class Horario(models.Model):
    """
    Modelo representando un horario (Matutino, verpertino, nocturno 7:840, 9-11am, etc).
    """
    name = models.CharField(max_length=100, help_text="Ingresa el horario de interés")

    def __str__(self):
        """
        String for representing the Model object (in Admin site etc.)
        """
        return self.name
        
class ProspectoAccion(models.Model):
    """
    Model representing a comment against a blog post.
    """
    descripcion = models.TextField(max_length=1000, help_text="Enter comment about blog here.")
    autor = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
      # Foreign Key used because ProspectoAcción can only have one autor/User, but users can have multiple actions
    accion_date = models.DateTimeField(auto_now_add=True)
    prospecto= models.ForeignKey(Prospecto, on_delete=models.CASCADE) # CASCADE si se borra el prospecto, también se borra la acción
    tipo_accion = models.ForeignKey('Accion', on_delete=models.SET_NULL, null=True, help_text="Selecciona el tipo de acción")
    
    class Meta:
        ordering = ["accion_date"]

    def __str__(self):
        """
        String for representing the Model object.
        """
        len_title=75
        if len(self.description)>len_title:
            titlestring=self.description[:len_title] + '...'
        else:
            titlestring=self.description
        return titlestring

# Acciones para desplegar lista con opciones
class Accion(models.Model):
    """
    Modelo que representa acciones como llamada, mail, comentario, examen de colocación
    """
    name = models.CharField(max_length=100, help_text="Ingresa los tipos de acción")

    def __str__(self):
        """
        String for representing the Model object (in Admin site etc.)
        """
        return self.name
        
# Razones de desinteres de un prospecto
class ProspectoRazon(models.Model):
    """
    Modelo que representa razones de desinteres como precio, ubicación, metodología, etc. 
    """
    comentario = models.TextField(max_length=2000, help_text='Agrega una nota u comentario')
    accion_date = models.DateTimeField(auto_now_add=True)
    prospecto= models.ForeignKey(Prospecto, on_delete=models.CASCADE) # CASCADE si se borra el prospecto, también se borra la acción
    tipo_razon = models.ForeignKey('Razon', on_delete=models.SET_NULL, null=True, help_text="Selecciona la razón principal de desinterés")

    class Meta:
        ordering = ["accion_date"]

    def __str__(self):
        """
        String for representing the Model object.
        """
        len_title=75
        if len(self.description)>len_title:
            titlestring=self.description[:len_title] + '...'
        else:
            titlestring=self.description
        return titlestring

class Razon(models.Model):
    """
    Modelo que representa acciones como llamada, mail, comentario, examen de colocación
    """
    name = models.CharField(max_length=100, help_text="Ingresa la(s) razon(es) de desinterés")

    def __str__(self):
        """
        String for representing the Model object (in Admin site etc.)
        """
        return self.name