from django.shortcuts import render

# Vista para Login
def login_view(request):
    return render(request, 'registration/login.html')  # Asegúrate que esté la ruta correcta de tu HTML

# Vista para Panel de Control
def panel(request):
    return render(request, 'registration/panel_de_control.html')  # Asegúrate de tener la ruta correcta
