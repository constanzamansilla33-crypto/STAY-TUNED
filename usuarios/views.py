from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from .forms import RegistroForm, CredencialMedicaForm
from .models import CredencialMedica
from django.contrib import messages
from django.views.decorators.cache import never_cache

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

    if request.method == 'POST':
        form = CredencialMedicaForm(
            request.POST,
            instance=credencial
        )

        if form.is_valid():
            credencial = form.save(commit=False)
            credencial.usuario = request.user
            credencial.save()

            messages.success(
                request,
                'Tu credencial médica se guardó correctamente.'
            )

            return redirect('perfil')
    else:
        form = CredencialMedicaForm(instance=credencial)

    return render(request, 'usuarios/credencial_medica.html', {
        'form': form
    })