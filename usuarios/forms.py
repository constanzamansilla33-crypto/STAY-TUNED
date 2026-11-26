from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import CredencialMedica
import re


class RegistroForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = [
            'username',
            'first_name',
            'last_name',
            'email',
            'password1',
            'password2',
        ]


class CredencialMedicaForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for nombre in [
        'contacto_principal_vinculo',
        'contacto_secundario_vinculo'
        ]:
        
            self.fields[nombre].choices = [
            ('', 'Seleccioná un vínculo')
        ] + CredencialMedica.VINCULOS

    class Meta:
        model = CredencialMedica

        fields = [
            'grupo_sanguineo',
            'tiene_alergias',
            'alergias',
            'tiene_condiciones_medicas',
            'condiciones_medicas',
            'toma_medicacion',
            'medicacion_habitual',
            'dosis_medicacion',
            'frecuencia_medicacion',
            'informacion_adicional',
            'contacto_principal_nombre',
            'contacto_principal_vinculo',
            'contacto_principal_otro_vinculo',
            'contacto_principal_telefono',
            'contacto_secundario_nombre',
            'contacto_secundario_vinculo',
            'contacto_secundario_otro_vinculo',
            'contacto_secundario_telefono',
        ]

        labels = {
            'grupo_sanguineo': 'Grupo sanguíneo',
            'tiene_alergias': '¿Tenés alergias?',
            'alergias': 'Especificá tus alergias',
            'tiene_condiciones_medicas': '¿Tenés alguna condición médica?',
            'condiciones_medicas': 'Especificá tus condiciones médicas',
            'toma_medicacion': '¿Tomás medicación habitual?',
            'medicacion_habitual': 'Nombre de los medicamentos',
            'dosis_medicacion': 'Dosis prescritas',
            'frecuencia_medicacion': 'Frecuencias prescritas',
            'informacion_adicional': 'Información adicional que te gustaría que sepamos',
            'contacto_principal_nombre': 'Nombre',
            'contacto_principal_vinculo': 'Vínculo',
            'contacto_principal_otro_vinculo': 'Especificá el vínculo',
            'contacto_principal_telefono': 'Teléfono',
            'contacto_secundario_nombre': 'Nombre',
            'contacto_secundario_vinculo': 'Vínculo',
            'contacto_secundario_otro_vinculo': 'Especificá el vínculo',
            'contacto_secundario_telefono': 'Teléfono',
        }

        widgets = {
            'alergias': forms.Textarea(attrs={'rows': 2}),
            'condiciones_medicas': forms.Textarea(attrs={'rows': 2}),
            'medicacion_habitual': forms.Textarea(attrs={'rows': 2}),
            'dosis_medicacion': forms.Textarea(attrs={'rows': 2}),
            'frecuencia_medicacion': forms.Textarea(attrs={'rows': 2}),
            'informacion_adicional': forms.Textarea(attrs={'rows': 3}),
            'contacto_principal_telefono': forms.TextInput(
                attrs={'type': 'tel'}
            ),
            'contacto_secundario_telefono': forms.TextInput(
                attrs={'type': 'tel'}
            ),
        }

    def validar_telefono(self, telefono):
        if telefono:
            if not re.fullmatch(r'\+?[0-9 ()-]+', telefono):
                raise forms.ValidationError(
                    'Ingresá un número de teléfono válido.'
                )

            cantidad = sum(c.isdigit() for c in telefono)

            if cantidad < 7 or cantidad > 15:
                raise forms.ValidationError(
                    'El teléfono debe contener entre 7 y 15 dígitos.'
                )

        return telefono

    def clean_contacto_principal_telefono(self):
        return self.validar_telefono(
            self.cleaned_data['contacto_principal_telefono']
        )

    def clean_contacto_secundario_telefono(self):
        return self.validar_telefono(
            self.cleaned_data['contacto_secundario_telefono']
        )
        
    def clean(self):
        datos = super().clean()

        if datos.get('tiene_alergias') == 'si':
            if not datos.get('alergias'):
                self.add_error(
                    'alergias',
                    'Especificá cuáles son tus alergias.'
                )

        if datos.get('tiene_condiciones_medicas') == 'si':
            if not datos.get('condiciones_medicas'):
                self.add_error(
                    'condiciones_medicas',
                    'Especificá tus condiciones médicas.'
                )

        if datos.get('toma_medicacion') == 'si':
            if not datos.get('medicacion_habitual'):
                self.add_error(
                    'medicacion_habitual',
                    'Indicá el nombre de los medicamentos.'
                )

            if not datos.get('dosis_medicacion'):
                self.add_error(
                    'dosis_medicacion',
                    'Indicá las dosis prescritas o escribí Desconocido.'
                )

            if not datos.get('frecuencia_medicacion'):
                self.add_error(
                    'frecuencia_medicacion',
                    'Indicá las frecuencias prescritas o escribí Desconocido.'
                )

        if datos.get('contacto_principal_vinculo') == 'otro':
            if not datos.get('contacto_principal_otro_vinculo'):
                self.add_error(
                    'contacto_principal_otro_vinculo',
                    'Especificá el vínculo.'
                )

        nombre = datos.get('contacto_secundario_nombre')
        vinculo = datos.get('contacto_secundario_vinculo')
        telefono = datos.get('contacto_secundario_telefono')
        otro_vinculo = datos.get('contacto_secundario_otro_vinculo')

        if any([nombre, vinculo, telefono, otro_vinculo]):
            if not nombre:
                self.add_error(
                    'contacto_secundario_nombre',
                    'Ingresá el nombre.'
                )

            if not vinculo:
                self.add_error(
                    'contacto_secundario_vinculo',
                    'Seleccioná un vínculo.'
                )

            if not telefono:
                self.add_error(
                    'contacto_secundario_telefono',
                    'Ingresá el teléfono.'
                )

            if vinculo == 'otro' and not otro_vinculo:
                self.add_error(
                    'contacto_secundario_otro_vinculo',
                    'Especificá el vínculo.'
                )

        if datos.get('tiene_alergias') != 'si':
            datos['alergias'] = ''

        if datos.get('tiene_condiciones_medicas') != 'si':
            datos['condiciones_medicas'] = ''

        if datos.get('toma_medicacion') != 'si':
            datos['medicacion_habitual'] = ''
            datos['dosis_medicacion'] = ''
            datos['frecuencia_medicacion'] = ''

        if datos.get('contacto_principal_vinculo') != 'otro':
            datos['contacto_principal_otro_vinculo'] = ''

        if datos.get('contacto_secundario_vinculo') != 'otro':
            datos['contacto_secundario_otro_vinculo'] = ''

        return datos