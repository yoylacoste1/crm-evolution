from django.shortcuts import render

# Vista para Login
def login_view(request):
    return render(request, 'registration/login.html')  
# Vista para Panel de Control
def panel(request):
    return render(request, 'registration/panel_de_control.html')  
