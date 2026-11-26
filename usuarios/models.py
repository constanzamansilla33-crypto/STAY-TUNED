from django.db import models
from django.conf import settings


class CredencialMedica(models.Model):

    GRUPOS_SANGUINEOS = [
        ('A+', 'A+'),
        ('A-', 'A-'),
        ('B+', 'B+'),
        ('B-', 'B-'),
        ('AB+', 'AB+'),
        ('AB-', 'AB-'),
        ('O+', 'O+'),
        ('O-', 'O-'),
        ('desconocido', 'Desconocido'),
    ]

    usuario = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='credencial_medica'
    )

    grupo_sanguineo = models.CharField(
        max_length=12,
        choices=GRUPOS_SANGUINEOS,
        default='desconocido',
        blank=True
    )

    alergias = models.TextField(blank=True)
    condiciones_medicas = models.TextField(blank=True)
    medicacion_habitual = models.TextField(blank=True)

    contacto_principal_nombre = models.CharField(max_length=100)
    contacto_principal_vinculo = models.CharField(max_length=50)
    contacto_principal_telefono = models.CharField(max_length=30)

    contacto_secundario_nombre = models.CharField(
        max_length=100,
        blank=True
    )

    contacto_secundario_vinculo = models.CharField(
        max_length=50,
        blank=True
    )

    contacto_secundario_telefono = models.CharField(
        max_length=30,
        blank=True
    )

    fecha_actualizacion = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Credencial médica de {self.usuario.username}"