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

    RESPUESTAS = [
        ('si', 'Sí'),
        ('no', 'No'),
        ('no_informado', 'No informado'),
    ]

    VINCULOS = [
        ('madre', 'Madre'),
        ('padre', 'Padre'),
        ('hermano', 'Hermano/a'),
        ('pareja', 'Pareja'),
        ('amigo', 'Amigo/a'),
        ('tutor', 'Tutor/a'),
        ('familiar', 'Otro familiar'),
        ('otro', 'Otro'),
    ]

    usuario = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='credencial_medica'
    )

    grupo_sanguineo = models.CharField(
        max_length=12,
        choices=GRUPOS_SANGUINEOS,
        default='desconocido'
    )

    tiene_alergias = models.CharField(
        max_length=15,
        choices=RESPUESTAS,
        default='no_informado'
    )

    alergias = models.TextField(blank=True)

    tiene_condiciones_medicas = models.CharField(
        max_length=15,
        choices=RESPUESTAS,
        default='no_informado'
    )

    condiciones_medicas = models.TextField(blank=True)

    toma_medicacion = models.CharField(
        max_length=15,
        choices=RESPUESTAS,
        default='no_informado'
    )

    informacion_adicional = models.TextField(blank=True)

    contacto_principal_nombre = models.CharField(
        max_length=100
    )

    contacto_principal_vinculo = models.CharField(
        max_length=50,
        choices=VINCULOS
    )

    contacto_principal_otro_vinculo = models.CharField(
        max_length=100,
        blank=True
    )

    contacto_principal_telefono = models.CharField(
        max_length=30
    )

    contacto_secundario_nombre = models.CharField(
        max_length=100,
        blank=True
    )

    contacto_secundario_vinculo = models.CharField(
        max_length=50,
        choices=VINCULOS,
        blank=True
    )

    contacto_secundario_otro_vinculo = models.CharField(
        max_length=100,
        blank=True
    )

    contacto_secundario_telefono = models.CharField(
        max_length=30,
        blank=True
    )

    fecha_actualizacion = models.DateTimeField(
        auto_now=True
    )

    def __str__(self):
        return f"Credencial médica de {self.usuario.username}"
    
class Medicamento(models.Model):

    credencial = models.ForeignKey(
        CredencialMedica,
        on_delete=models.CASCADE,
        related_name='medicamentos'
    )

    nombre = models.CharField(max_length=150)

    dosis_frecuencia = models.TextField(max_length=500)

    def __str__(self):
        return self.nombre