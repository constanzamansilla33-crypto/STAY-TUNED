
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from eventos.models import Evento, Sector
from .models import SolicitudAsistencia



def solicitar_asistencia(request, pk):
    evento = get_object_or_404(Evento, pk=pk, activo=True)
    sectores = Sector.objects.filter(evento=evento)

    if request.method == 'POST':
        tipo = request.POST.get('tipo')
        descripcion = request.POST.get('descripcion', '').strip()
        sector_id = request.POST.get('sector')

        tipos_validos = [opcion[0] for opcion in SolicitudAsistencia.TIPOS]

        if tipo not in tipos_validos:
            messages.error(request, 'Seleccioná un tipo de asistencia válido.')

        elif tipo == 'otro' and not descripcion:
            messages.error(request, 'Contanos qué tipo de ayuda necesitás.')

        else:
            sector = None

            if sector_id:
                sector = get_object_or_404(
                    Sector, pk=sector_id, evento=evento
                )

            SolicitudAsistencia.objects.create(
                evento=evento,
                sector=sector,
                tipo=tipo,
                descripcion=descripcion
            )

            messages.success(
                request,
                '¡Su solicitud fue enviada correctamente! Aguarde con calma, un miembro del staff se acercará a asistirlo.'
            )

            return redirect('solicitar_asistencia', pk=evento.pk)

    return render(request, 'asistencia/solicitar.html', {
        'evento': evento,
        'sectores': sectores,
        'tipos': SolicitudAsistencia.TIPOS,
    })
