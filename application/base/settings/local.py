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
