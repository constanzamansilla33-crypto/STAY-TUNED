from django.db import models


class Evento(models.Model):
    nombre = models.CharField(max_length=150)
    artista = models.CharField(max_length=150)
    fecha = models.DateField(
    blank=True,
    null=True,
    verbose_name="Fecha del evento"
)
    lugar = models.CharField(
    max_length=150,
    blank=True,
    verbose_name="Estadio / recinto"
)

    ciudad = models.CharField(
    max_length=150,
    blank=True,
    verbose_name="Ciudad"
)
    
    pais = models.CharField(
    max_length=100,
    blank=True,
    verbose_name="País"
)

    mapa_url = models.URLField(
    blank=True,
    verbose_name="Enlace de Google Maps"
)

    descripcion = models.TextField(blank=True)
    setlist = models.TextField(blank=True)
    imagen = models.ImageField(upload_to='eventos/', blank=True, null=True)
    
    plano = models.ImageField(
    upload_to='planos/',
    blank=True,
    null=True,
    verbose_name="Plano del recinto"
)
    
    activo = models.BooleanField(default=True)
    hora = models.TimeField(
    blank=True,
    null=True,
    verbose_name="Hora del evento"
)

    def __str__(self):
        return self.nombre
    
    @property
    def canciones_setlist(self):
        return [
            cancion.strip()
            for cancion in self.setlist.splitlines()
            if cancion.strip()
        ]
    
    
class Sector(models.Model):
    evento = models.ForeignKey(Evento, on_delete=models.CASCADE, related_name='sectores')
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField(blank=True)
    capacidad = models.PositiveIntegerField(null=True, blank=True)
    
    posicion_x = models.DecimalField(
    max_digits=5,
    decimal_places=2,
    null=True,
    blank=True
)

    posicion_y = models.DecimalField(
    max_digits=5,
    decimal_places=2,
    null=True,
    blank=True
)

    def __str__(self):
        return f"{self.nombre} - {self.evento.nombre}"
    

class ServicioEvento(models.Model):
    TIPOS = [
        ('banio', 'Baño'),
        ('medico', 'Puesto médico'),
        ('agua', 'Agua'),
        ('acceso', 'Acceso'),
        ('salida', 'Salida'),
        ('otro', 'Otro'),
    ]

    evento = models.ForeignKey(Evento, on_delete=models.CASCADE, related_name='servicios')
    sector = models.ForeignKey(Sector, on_delete=models.SET_NULL, null=True, blank=True)
    nombre = models.CharField(max_length=100)
    tipo = models.CharField(max_length=20, choices=TIPOS)
    descripcion = models.TextField(blank=True)
    
    posicion_x = models.DecimalField(
    max_digits=5,
    decimal_places=2,
    null=True,
    blank=True
)

    posicion_y = models.DecimalField(
    max_digits=5,
    decimal_places=2,
    null=True,
    blank=True
)

    def __str__(self):
        return self.nombre
    
    
class Aviso(models.Model):
    evento = models.ForeignKey(Evento, on_delete=models.CASCADE, related_name='avisos')
    titulo = models.CharField(max_length=150)
    mensaje = models.TextField()
    fecha_publicacion = models.DateTimeField(auto_now_add=True)
    importante = models.BooleanField(default=False)

    def __str__(self):
        return self.titulo