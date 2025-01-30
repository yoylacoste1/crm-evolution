from django.urls import path
from . import views  # Importar las vistas de la app

urlpatterns = [
    path('', views.login_view, name='login'),  
    path('panel/', views.panel, name='panel_control'),
]
