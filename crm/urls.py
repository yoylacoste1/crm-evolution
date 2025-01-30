from django.contrib import admin  # Asegúrate de importar admin aquí
from django.urls import path
from . import views

app_name = 'crm'  # Define el namespace para las URLs de esta app

urlpatterns = [
    path('admin/', admin.site.urls, name='admin'),  # Acceso al admin
    path('test/', views.test_view, name='test_view'),
    path('login/', views.login_view, name='login'),
    path('panel/', views.panel_view, name='panel_control'),
    path('agendado/', views.agendado_view, name='agendado'),
    path('asignacion/', views.asignacion_view, name='asignacion'),
    path('chat/', views.chat_view, name='chat'),
    path('clientes/', views.clientes_view, name='clientes'),
    path('configuracion/', views.configuracion_view, name='configuracion'),
    path('estadisticas/', views.estadisticas_view, name='estadisticas'),
    path('estatus/', views.estatus_view, name='estatus'),
    path('integracion/', views.integracion_view, name='integracion'),
    path('soporte/', views.soporte_view, name='soporte'),
    path('', views.login_view, name='login'),  # Redirige a login por defecto
]
