"""
Django settings for rest_project project.

Generated by 'django-admin startproject' using Django 1.10.4.

For more information on this file, see
https://docs.djangoproject.com/en/1.10/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.10/ref/settings/
"""

#HEROKU:settings
import dj_database_url
import os

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.10/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
#SECRET_KEY = config('SECRET_KEY')
SECRET_KEY = '%6)&_x54bdqyn@z-z9^&w+cyy*m(q@77*2gddm#lk)z93wxxca'
# SECURITY WARNING: don't run with debug turned on in production!

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'whitenoise.runserver_nostatic',
    'django_pgviews',
    'rest_framework',
    'djgeojson',
    'leaflet',
    'corsheaders',
    'django_datatables_view',
    'wsn',
]

MIDDLEWARE_CLASSES = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    ]


ROOT_URLCONF = 'rest_project.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True, #CARGA AUTOMATICAMENTE LOS TEMPLATE DE LOS SUBDIRECTORIOS
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

#db_from_env = dj_database_url.config(conn_max_age=500)
#DATABASES['default'].update(db_from_env)
#DATABASES = {'default': db_from_env}

# Honor the 'X-Forwarded-Proto' header for request.is_secure()
SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https') #HK_ST
# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.8/howto/static-files/

DATABASES = {'default': dj_database_url.config(default='postgres://user:pass@localhost/dbname')}

#DATABASES['default'] = dj_database_url.config() #HK_ST

ALLOWED_HOSTS = ['*'] #HK_ST

DEBUG = False #HK_ST

#HK_ST
try:
    from .local_settings import *
except ImportError:
    pass

WSGI_APPLICATION = 'rest_project.wsgi.application'

# Internationalization
# https://docs.djangoproject.com/en/1.8/topics/i18n/

LANGUAGE_CODE = 'es'

TIME_ZONE = 'America/Argentina/Buenos_Aires'

USE_I18N = True

USE_L10N = True

USE_TZ = False

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.8/howto/static-files/

#esto esta en la documentacion de django. Como seleccionar y apuntar a los directoreos estaticos
#PROJECT_ROOT = os.path.dirname(os.path.abspath(__file__))
#BASE_DIR = os.path.dirname(os.path.abspath(__file__))
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.9/howto/static-files/
STATIC_URL = '/static/'
#STATIC_URL = 'staticfiles/'
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
#STATIC_ROOT = os.path.join(PROJECT_ROOT, 'staticfiles')

# Extra places for collectstatic to find static files.
STATICFILES_DIRS = [
    os.path.join(BASE_DIR,'wsn','static'),
    #'wsn/static/',
]

# Simplified static file serving.
# https://warehouse.python.org/project/whitenoise/

STATICFILES_STORAGE = 'whitenoise.django.GzipManifestStaticFilesStorage'

#Cors settings
CORS_ORIGIN_ALLOW_ALL = True
CORS_ALLOW_CREDENTIALS = True

#LOGIN SETTINGS (Default)
LOGIN_REDIRECT_URL='/wsn/lab-test/'
LOGIN_URL = '/wsn/login/'
#LOGOUT_REDIRECT_URL = '/wsn/login'

# Por defecto, sin poner estas lineas se carga estos dos renderizadores.
# Si solo queremos mostrar dejamos el JSONRenderer y listo, mostramos los datos.
# Tmb se puede cargar por defecto el parser
REST_FRAMEWORK = {
    'DEFAULT_RENDERER_CLASSES': (
        'rest_framework.renderers.JSONRenderer',
        'rest_framework.renderers.BrowsableAPIRenderer',
    ),
    #'DEFAULT_PARSER_CLASSES': (
    #        'rest_framework.parsers.JSONParser',
    #)
}

#leaflet django settings (solo para el Adminsite. Para el template lo generamos a pata)
LEAFLET_CONFIG = {
    # lim. del mapa (centro inicial y zoom)
    'DEFAULT_CENTER': (-31.416667, -64.183333),
    'DEFAULT_ZOOM': 7,
    'MIN_ZOOM': 5,
    'MAX_ZOOM': 17,
    #Capa principal
    'TILES': [
    ('Satelite', '//server.arcgisonline.com/ArcGIS/rest/services/World_Imagery/MapServer/tile/{z}/{y}/{x}', {'attribution': ' Power by Esri | Source: Esri, i-cubed, USDA, USGS, AEX, GeoEye, Getmapping, Aerogrid, IGN, IGP, UPR-EGP, and the GIS User Community'}),
    ('OStreetMap', 'http://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png' , {'attribution': '&copy; OpenStreetMap'}),
    ],
}
