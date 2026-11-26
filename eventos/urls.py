from django.urls import path
from . import views

urlpatterns = [
    path('', views.inicio, name='inicio'),
    path('evento/<int:pk>/', views.detalle_evento, name='detalle_evento'),
    path('service-worker.js', views.service_worker, name='service_worker'),
]