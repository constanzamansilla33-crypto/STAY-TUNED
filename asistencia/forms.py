from django import forms
from .models import SolicitudAsistencia
from eventos.models import Sector


class SolicitudAsistenciaForm(forms.ModelForm):

    descripcion = forms.CharField(
        required=False,
        widget=forms.Textarea(attrs={'rows': 4})
    )

    def __init__(self, *args, evento, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['sector'].queryset = Sector.objects.filter(
            evento=evento
        )

        self.fields['sector'].empty_label = 'No estoy seguro/a'

    class Meta:
        model = SolicitudAsistencia

        fields = [
            'tipo',
            'sector',
            'descripcion',
        ]

        widgets = {
            'tipo': forms.RadioSelect(),
        }

    def clean(self):
        datos = super().clean()

        if datos.get('tipo') == 'otro':
            if not datos.get('descripcion'):
                self.add_error(
                    'descripcion',
                    'Contanos qué tipo de ayuda necesitás.'
                )

        return datos