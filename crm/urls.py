from django.urls import path
from . import views

urlpatterns = [
    path('', views.dashboard, name='dashboard'),
]

from django.urls import path
from . import views  # Asegúrate de importar las vistas de tu app

urlpatterns = [
    # Otras rutas que ya tengas configuradas
    path('panel/', views.panel, name='panel_control'),  # Nueva ruta para el Panel de Control
]

