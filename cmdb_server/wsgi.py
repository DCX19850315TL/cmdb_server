"""
WSGI config for cmdb_server project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.11/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application
from put.lib.http_request import HttpRequest
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "cmdb_server.settings")

application = get_wsgi_application()
application.request_class = HttpRequest