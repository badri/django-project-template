from .default import *

DEBUG = True
TEMPLATE_DEBUG = DEBUG

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2', 
        'NAME': '',                     
        'USER': '',                    
        'PASSWORD': '',               
        'HOST': 'localhost',                  
        'PORT': '',                 
    }
}


THIRDPARTY_APPS += [
    'django_nose',
]


INSTALLED_APPS = DJANGO_APPS + THIRDPARTY_APPS + CUSTOM_APPS
