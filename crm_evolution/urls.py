from django.contrib import admin
from django.urls import path, include

# Aquí van las URLs principales de tu proyecto
urlpatterns = [
    path('admin/', admin.site.urls),  # Acceso al panel de administración de Django
    path('', include('crm.urls')),    # Acceso a las URLs de la app 'crm'
    path('accounts/', include('django.contrib.auth.urls')),  # URLs de autenticación de Django (login, logout, etc.)
]


