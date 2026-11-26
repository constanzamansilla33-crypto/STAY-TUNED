from django.contrib import admin
from .models import Evento, Sector, ServicioEvento, Aviso
from django.db import models
from django import forms

class EventoForm(forms.ModelForm):

    class Meta:
        model = Evento
        fields = "__all__"
        help_texts = {
            "setlist": "Ingresá las canciones separadas por comas. La numeración se genera automáticamente."
        }

    def clean_setlist(self):
        setlist = self.cleaned_data.get("setlist", "")

        canciones = [
            cancion.strip()
            for cancion in setlist.replace("\n", " ").replace("\r", " ").split(",")
            if cancion.strip()
        ]

        return "\n".join(canciones)

@admin.register(Evento)
class EventoAdmin(admin.ModelAdmin):
    form = EventoForm

    fields = (
        'nombre',
        'artista',
        'fecha',
        'hora',
        'lugar',
        'ciudad',
        'pais',
        'mapa_url',
        'descripcion',
        'setlist',
        'imagen',
        'plano',
        'activo',
    )

    formfield_overrides = {
        models.DateField: {
            'widget': admin.widgets.AdminDateWidget
        },
        models.TimeField: {
    'widget': forms.TimeInput(
        attrs={'type': 'time'},
        format='%H:%M'
    )
},
    }
        
@admin.register(Sector)
class SectorAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'evento', 'posicion_x', 'posicion_y')
    list_filter = ('evento',)


@admin.register(ServicioEvento)
class ServicioEventoAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'tipo', 'evento', 'posicion_x', 'posicion_y')
    list_filter = ('evento', 'tipo')


admin.site.register(Aviso)