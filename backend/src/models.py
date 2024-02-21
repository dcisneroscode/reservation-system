from django.db import models


class Habitacion(models.Model):
    numero = models.CharField(max_length=10, unique=True)
    tipo = models.CharField(max_length=100)
    descripcion = models.TextField()
    disponible = models.BooleanField(default=True)
    version = models.IntegerField(default=1)

    def __str__(self):
        return self.numero

class Reservacion(models.Model):
    habitacion = models.ForeignKey(Habitacion, on_delete=models.CASCADE)
    nombre_cliente = models.CharField(max_length=100)
    fecha_inicio = models.DateTimeField()
    fecha_fin = models.DateTimeField()
    creado_en = models.DateTimeField(auto_now_add=True)
    modificado_en = models.DateTimeField(auto_now=True)
    confirmada = models.BooleanField(default=False)

    def __str__(self):
        return f"Reserva de {self.habitacion} para {self.nombre_cliente}"
