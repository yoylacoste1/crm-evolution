from django.shortcuts import render


def test_view(request):
    return render(request, 'registration/tes.html')  

def login_view(request):
    return render(request, 'registration/login.html')

def panel_view(request):
    return render(request, 'registration/panel de control.html')

def agendado_view(request):
    return render(request, 'registration/agendado.html')

def asignacion_view(request):
    return render(request, 'registration/asignacion.html')

def chat_view(request):
    return render(request, 'registration/chat.html')

def clientes_view(request):
    return render(request, 'registration/clientes.html')

def configuracion_view(request):
    return render(request, 'registration/configuracion.html')

def estadisticas_view(request):
    return render(request, 'registration/estadisticas.html')

def estatus_view(request):
    return render(request, 'registration/estatus.html')

def integracion_view(request):
    return render(request, 'registration/integracion.html')

def soporte_view(request):
    return render(request, 'registration/soporte.html')
