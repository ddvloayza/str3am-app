"""
WSGI config for dockerizeddjango project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/2.1/howto/deployment/wsgi/
"""

import os
import sys
from os.path import dirname, realpath

BASE_DIR = dirname(realpath(__file__))
sys.path = [BASE_DIR] + sys.path

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'settings.prod')

application = get_wsgi_application()
