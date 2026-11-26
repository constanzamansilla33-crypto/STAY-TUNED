from django.db.models import Q
from django.shortcuts import render, get_object_or_404
from .models import Evento
from pathlib import Path
from django.conf import settings
from django.http import HttpResponse


def inicio(request):
    busqueda = request.GET.get('buscar', '').strip()

    eventos = Evento.objects.filter(activo=True).order_by('fecha')

    if busqueda:
        eventos = eventos.filter(
            Q(nombre__icontains=busqueda) |
            Q(artista__icontains=busqueda)
        )

    return render(request, 'eventos/inicio.html', {
        'eventos': eventos,
        'busqueda': busqueda
    })


def detalle_evento(request, pk):
    evento = get_object_or_404(Evento, pk=pk, activo=True)

    return render(request, 'eventos/detalle.html', {
        'evento': evento
    })
    
def service_worker(request):
    archivo = (
        Path(settings.BASE_DIR)
        / 'eventos'
        / 'static'
        / 'eventos'
        / 'service-worker.js'
    )

    contenido = archivo.read_text(encoding='utf-8')

    return HttpResponse(
        contenido,
        content_type='application/javascript'
    )