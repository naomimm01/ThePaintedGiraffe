import os

from django.core.asgi import get_asgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'painted_giraffe.settings')

application = get_asgi_application()
