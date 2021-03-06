from unipath import Path

PROJECT_ROOT = Path(__file__).ancestor(3)

MEDIA_ROOT = PROJECT_ROOT.child('media')

STATIC_ROOT = PROJECT_ROOT.child('static')

BOWER_COMPONENTS_ROOT = PROJECT_ROOT.child('components')

STATICFILES_DIRS = (
    PROJECT_ROOT.child('assets'),
)

TEMPLATE_DIRS = (
    PROJECT_ROOT.child('templates'),
)

DEBUG = False
TEMPLATE_DEBUG = DEBUG

ADMINS = (
    ('Your Name', 'your_email@example.com'),
)

MANAGERS = ADMINS

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.', 
        'NAME': '',                     
        'USER': '',                    
        'PASSWORD': '',               
        'HOST': '',                  
        'PORT': '',                 
    }
}

TIME_ZONE = 'America/Chicago'

LANGUAGE_CODE = 'en-us'

SITE_ID = 1

USE_I18N = True

USE_L10N = True

USE_TZ = True


MEDIA_URL = '/media/'


STATIC_URL = '/static/'


STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
    'djangobower.finders.BowerFinder',
)

SECRET_KEY = r"6e!=_4n%a(dmjbg!v8w6!bq^k)ho_7u&q0hp*t2dq%7cm%+2!w"

TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
)

MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
)

ROOT_URLCONF = 'kalvi.urls'

WSGI_APPLICATION = 'kalvi.wsgi.application'

DJANGO_APPS = [
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]


THIRDPARTY_APPS = [
    #'grappelli',
    'django.contrib.admin',  # This has to be here because of Grappelli
    'south',
    'userena',
    'guardian',
    'taggit',
    'rest_framework',
    'pipeline',
    'djangobower',
]

# add custom apps here
CUSTOM_APPS = [
    'accounts',
]

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'filters': {
        'require_debug_false': {
            '()': 'django.utils.log.RequireDebugFalse'
        }
    },
    'handlers': {
        'mail_admins': {
            'level': 'ERROR',
            'filters': ['require_debug_false'],
            'class': 'django.utils.log.AdminEmailHandler'
        }
    },
    'loggers': {
        'django.request': {
            'handlers': ['mail_admins'],
            'level': 'ERROR',
            'propagate': True,
        },
    }
}

# pipeline stuff
from .pipeline import *
# user authentication stuff
from .auth import *
# bower components
from .bower import *
