from pathlib import Path
from dotenv import load_dotenv
import os

#region BASIC SETTINGS & DEPLOYMENT
BASE_DIR = Path(__file__).resolve().parent.parent
ROOT_URLCONF = 'base.urls'
WSGI_APPLICATION = 'base.wsgi.application'
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'


load_dotenv()
SECRET_KEY = os.environ.get('SECRET_KEY')

DEBUG = True
ALLOWED_HOSTS = []
#endregion BASIC SETTINGS & DEPLOYMENT

INSTALLED_APPS = [
    
    'admin_tools_stats',  
    'django_nvd3',
    'jazzmin',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    #third party apps
    'crispy_forms',
    "crispy_bootstrap5",
    #custom apps
    'app',
]

#region CRISPY_FORMS_SETTINGS
CRISPY_ALLOWED_TEMPLATE_PACKS = "bootstrap5"
CRISPY_TEMPLATE_PACK = "bootstrap5"
#endregion CRISPY_FORMS_SETTINGS

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]


TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR, 'templates'],
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

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',  
        'NAME': 'tim_user',
        'USER': 'tim_user',
        'PASSWORD': 'tim_user',
    }
}

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

#region LANGUAGE & TIME
LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'Europe/Berlin'
USE_I18N = True
USE_TZ = True
#endregion LANGUAGE & TIME

#region STATIC & MEDIA FILES
STATIC_URL = 'static/'
#endregion STATIC & MEDIA FILES

LOGIN_REDIRECT_URL = '/home'
LOGOUT_REDIRECT_URL = '/login'
