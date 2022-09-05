from distutils.command.upload import upload
from django.db import models

# Create your models here.
class Grupos(models.Model):

    grupo= models.CharField(max_length=255)
    nombre= models.CharField(max_length=255)
    fecha= models.IntegerField( )
    imagen= models.ImageField(upload_to="selecciones", null=True)
    