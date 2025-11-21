from django.db import models

class Repartidor(models.Model):
    ESTADO_REPARTIDOR = [
        ('disponible', 'Disponible'),
        ('ocupado', 'Ocupado'),
        ('inactivo', 'Inactivo'),
    ]

    nombre = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    telefono = models.CharField(max_length=15)
    vehiculo = models.CharField(max_length=50)
    placa = models.CharField(max_length=20)
    estado = models.CharField(max_length=10, choices=ESTADO_REPARTIDOR, default='disponible')
    calificacion = models.DecimalField(max_digits=3, decimal_places=2, default=0)

    def __str__(self):
        return self.nombre



# Create your models here.
