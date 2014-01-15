import os

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "{{ project_name }}.settings.live")
from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()
