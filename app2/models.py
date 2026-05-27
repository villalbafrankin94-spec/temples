from django.db import models

class Restaurante(models.Model):
    CATEGORIA_RESTAURANTE = [
        ('rapida', 'Comida rápida'),
        ('mexicana', 'Comida mexicana'),
        ('italiana', 'Comida italiana'),
        ('asiatica', 'Comida asiática'),
        ('vegetariana', 'Comida vegetariana'),
    ]

    nombre = models.CharField(max_length=100)
    propietario = models.CharField(max_length=100)
    email = models.EmailField()
    telefono = models.CharField(max_length=15)
    direccion = models.TextField(max_length=200)
    categoria = models.CharField(max_length=20, choices=CATEGORIA_RESTAURANTE)
    horario_apertura = models.TimeField()
    horario_cierre = models.TimeField()
    activo = models.BooleanField(default=True)
    calificacion_promedio = models.DecimalField(max_digits=3, decimal_places=2, default=0)

    def __str__(self):
        return self.nombre

# Create your models here.
