from django.db import models

# Create your models here.
class registros(models.Model): 
    name = models.CharField(max_length=60, null=False)
    email = models.CharField(max_length=100, null=False, unique=True)
    password = models.CharField(max_length=60, null=False)




class formulario(models.Model):
        pregunta1 = models.CharField(max_length=200)
        pregunta2 = models.CharField(max_length=200)
        pregunta3 = models.CharField(max_length=200)
        pregunta4 = models.CharField(max_length=200)
        pregunta5 = models.CharField(max_length=200)
        pregunta6 = models.CharField(max_length=200)
        pregunta7 = models.CharField(max_length=200)
        pregunta8 = models.CharField(max_length=200)
        pregunta9 = models.CharField(max_length=200)
        pregunta10 = models.CharField(max_length=200)