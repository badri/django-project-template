from .default import *

DEBUG = False
TEMPLATE_DEBUG = DEBUG

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2', 
        'NAME': '',                     
        'USER': '',                    
        'PASSWORD': '',               
        'HOST': '',                  
        'PORT': '',                 
    }
}
