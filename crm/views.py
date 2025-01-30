from django.shortcuts import render

# Vista para prueba
def test_view(request):
    return render(request, 'registration/tes.html')  

# Vista para Login
def login_view(request):
    return render(request, 'registration/login.html')  

# Vista para Panel de Control
def panel_view(request):
    return render(request, 'registration/panel de control.html')

# Vista para Agendado
def agendado_view(request):
    return render(request, 'registration/agendado.html')

# Vista para Asignación
def asignacion_view(request):
    return render(request, 'registration/asignacion.html')

# Vista para Chat
def chat_view(request):
    return render(request, 'registration/chat.html')

# Vista para Clientes
def clientes_view(request):
    return render(request, 'registration/clientes.html')

# Vista para Configuración
def configuracion_view(request):
    return render(request, 'registration/configuracion.html')

# Vista para Estadísticas
def estadisticas_view(request):
    return render(request, 'registration/estadisticas.html')

# Vista para Estatus
def estatus_view(request):
    return render(request, 'registration/estatus.html')

# Vista para Integración
def integracion_view(request):
    return render(request, 'registration/integracion.html')

# Vista para Soporte
def soporte_view(request):
    return render(request, 'registration/soporte.html')

# Vista para Panel de Control (versión correcta)
def panel(request):
    return render(request, 'registration/panel_de_control.html')
