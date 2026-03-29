from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone 

# Modelo Proyecto
class Proyecto(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.nombre


# Modelo Tarea
class Tarea(models.Model):
    titulo = models.CharField(max_length=100)
    descripcion = models.TextField()
    completado = models.BooleanField(default=False)
    fecha_creacion = models.DateTimeField(auto_now_add=True)  # Fecha de creación
    fecha_vencimiento = models.DateField(null=True, blank=True)  # Fecha de vencimiento opcional
    proyecto = models.ForeignKey(Proyecto, on_delete=models.CASCADE)

    def __str__(self):
        return self.titulo

    #Aquí va el método/propiedad estado
    #Sirve para que en el template uses {{ tarea.estado }}
    @property
    def estado(self):
        return "Completado" if self.completado else "Pendiente"