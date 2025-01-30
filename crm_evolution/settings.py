import os
import os
from pathlib import Path
from dotenv import load_dotenv
import dj_database_url

# Definir BASE_DIR
BASE_DIR = Path(__file__).resolve().parent.parent

# Carga el archivo .env
load_dotenv()

# Lee la clave secreta desde .env
SECRET_KEY = os.getenv('SECRET_KEY')

# Asegúrate de que DEBUG esté configurado correctamente
DEBUG = os.getenv('DEBUG') == 'True'

# Lee los hosts permitidos desde .env
ALLOWED_HOSTS = os.getenv('ALLOWED_HOSTS', '').split(',')

# Configura la base de datos usando DATABASE_URL
DATABASES = {
    'default': dj_database_url.config(default=os.getenv('DATABASE_URL'))
}

# Configuración de las aplicaciones instaladas
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'crm',  # Agregamos la app principal
]

# Middleware
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

# Configuración de las URLs
ROOT_URLCONF = 'crm_evolution.urls'

# Configuración de templates
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'crm', 'templates')],  # Ubicación correcta de las plantillas
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

# Configuración de WSGI
WSGI_APPLICATION = 'crm_evolution.wsgi.application'

# Configuración estática y media
STATIC_URL = '/static/'
STATICFILES_DIRS = [os.path.join(BASE_DIR, 'crm', 'static')]

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

# Otras configuraciones de Django
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
