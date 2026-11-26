from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from .models import CredencialMedica
from django.contrib import messages
from django.views.decorators.cache import never_cache
from .forms import RegistroForm, CredencialMedicaForm, MedicamentoFormSet
from django.db import transaction

def registro(request):
    if request.method == 'POST':
        form = RegistroForm(request.POST)

        if form.is_valid():
            usuario = form.save()
            login(request, usuario)
            return redirect('credencial_medica')
    else:
        form = RegistroForm()

    return render(request, 'usuarios/registro.html', {
        'form': form
    })


@login_required
@never_cache
def perfil(request):
    return render(request, 'usuarios/perfil.html')

@login_required
@never_cache
def credencial_medica(request):
    credencial = CredencialMedica.objects.filter(
        usuario=request.user
    ).first()

    if credencial is None:
        credencial = CredencialMedica(usuario=request.user)

    if request.method == 'POST':
        form = CredencialMedicaForm(
            request.POST,
            instance=credencial
        )

        formset = MedicamentoFormSet(
            request.POST,
            instance=credencial
        )

        formulario_valido = form.is_valid()
        medicamentos_validos = formset.is_valid()

        if formulario_valido and medicamentos_validos:

            toma_medicacion = form.cleaned_data['toma_medicacion']

            medicamentos = [
                medicamento
                for medicamento in formset.cleaned_data
                if medicamento.get('nombre')
                and not medicamento.get('DELETE')
            ]

            if toma_medicacion == 'si' and not medicamentos:
                form.add_error(
                    'toma_medicacion',
                    'Agregá al menos un medicamento.'
                )

            else:
                with transaction.atomic():
                    credencial = form.save(commit=False)
                    credencial.usuario = request.user
                    credencial.save()

                    formset.instance = credencial

                    if toma_medicacion == 'si':
                        formset.save()
                    else:
                        credencial.medicamentos.all().delete()

                messages.success(
                    request,
                    'Tu credencial médica se guardó correctamente.'
                )

                return redirect('perfil')

    else:
        form = CredencialMedicaForm(instance=credencial)

        formset = MedicamentoFormSet(instance=credencial)

    return render(request, 'usuarios/credencial_medica.html', {
        'form': form,
        'formset': formset
    })