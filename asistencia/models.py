from django.db import models
from eventos.models import Evento, Sector


class SolicitudAsistencia(models.Model):
    TIPOS = [
        ('medica', 'Asistencia médica'),
        ('seguridad', 'Seguridad'),
        ('orientacion', 'Orientación'),
        ('otro', 'Otro'),
    ]

    ESTADOS = [
        ('recibida', 'Recibida'),
        ('asignada', 'Asignada'),
        ('en_proceso', 'En proceso'),
        ('resuelta', 'Resuelta'),
    ]

    evento = models.ForeignKey(Evento, on_delete=models.CASCADE)
    sector = models.ForeignKey(Sector, on_delete=models.SET_NULL, null=True, blank=True)
    tipo = models.CharField(max_length=20, choices=TIPOS)
    descripcion = models.TextField()
    estado = models.CharField(max_length=20, choices=ESTADOS, default='recibida')
    fecha_creacion = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.get_tipo_display()} - {self.evento.nombre}"
