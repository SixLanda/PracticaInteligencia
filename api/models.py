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


class Task(models.Model):
    STATUS_CHOICES = [
        ('pendiente', 'Pendiente'),
        ('completada', 'Completada'),
    ]
    TYPE_CHOICES = [
        ('general', 'General'),
        ('recordatorio', 'Recordatorio'),
    ]

    title = models.CharField(max_length=100)
    detail = models.TextField()
    creation_date = models.DateTimeField()
    due_date = models.DateTimeField()
    status = models.CharField(max_length=10, choices=STATUS_CHOICES)
    type = models.CharField(max_length=12, choices=TYPE_CHOICES)

    def __str__(self):
        return self.title
