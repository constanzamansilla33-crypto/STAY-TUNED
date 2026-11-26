
from django.urls import path
from . import views

urlpatterns = [
    path(
        'evento/<int:pk>/solicitar-asistencia/',
        views.solicitar_asistencia,
        name='solicitar_asistencia'
    ),
]
