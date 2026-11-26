from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from eventos.models import Evento, Sector
from .models import SolicitudAsistencia
from .forms import SolicitudAsistenciaForm


def solicitar_asistencia(request, pk):
    evento = get_object_or_404(Evento, pk=pk, activo=True)

    if request.method == 'POST':
        form = SolicitudAsistenciaForm(
            request.POST,
            evento=evento
        )

        if form.is_valid():
            solicitud = form.save(commit=False)
            solicitud.evento = evento
            solicitud.save()

            messages.success(
                request,
                '¡Su solicitud fue enviada correctamente! Aguarde con calma, un miembro del staff se acercará a asistirlo.'
            )

            return redirect(
                'solicitar_asistencia',
                pk=evento.pk
            )

    else:
        form = SolicitudAsistenciaForm(evento=evento)

    return render(request, 'asistencia/solicitar.html', {
        'evento': evento,
        'form': form,
        'sectores': Sector.objects.filter(evento=evento),
        'tipos': SolicitudAsistencia.TIPOS,
    })