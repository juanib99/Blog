from distutils.command.upload import upload
from django.db import models

# Create your models here.
class Blog(models.Model):
    id = models.AutoField(primary_key=True, unique=True)
    titulo = models.CharField(max_length=100, verbose_name='Titulo')
    subtitulo = models.CharField(max_length=100, verbose_name='Subtitulo')
    texto = models.TextField()
    autor = models.CharField(max_length=40, verbose_name='Autor')
    fecha = models.DateTimeField()
    imagen = models.ImageField(upload_to='imagenes/')

    def __str__(self):
        fila = "Titulo: " + self.titulo
        return fila
    
    # def delete(self, using=None, keep_parents:False):
    #     self.imagen.storage.delete()
    #     super().delete()