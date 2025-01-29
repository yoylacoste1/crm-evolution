from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Contact, Task

@login_required
def dashboard(request):
    contacts = Contact.objects.filter(owner=request.user)
    tasks = Task.objects.filter(owner=request.user, completed=False).order_by('due_date')
    return render(request, 'crm/dashboard.html', {'contacts': contacts, 'tasks': tasks})

from django.shortcuts import render

def panel(request):
    return render(request, 'registration/panel de control.html')  # Ruta al archivo HTML
