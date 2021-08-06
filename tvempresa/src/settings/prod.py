# -*- coding: utf-8 -*-
# production.py
import os
from .base import *
import raven

DEBUG = True
PREPEND_WWW = False


# DIRS

MEDIA_ROOT = os.environ["MEDIA_ROOT"]
MEDIA_URL = os.environ["MEDIA_URL"]

STATIC_ROOT = os.environ.setdefault("STATIC_ROOT", "")
STATIC_URL = os.environ.setdefault("STATIC_URL", "")


STATICFILES_DIRS = (
    os.path.join(os.path.dirname(BASE_DIR), "static"),
)

ALLOWED_HOSTS = os.environ.setdefault("ALLOWED_HOSTS", [])

INSTALLED_APPS.append('raven.contrib.django.raven_compat')
# SESSIONS

SESSION_EXPIRE_AT_BROWSER_CLOSE = True

# SMART SELECT
JQUERY_URL = False

# CACHE
CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.db.DatabaseCache',
        'LOCATION': 'cache_table',
        'TIMEOUT': '300',
    }
}


TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(os.path.dirname(BASE_DIR), 'templates')],
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

# RAVEN_CONFIG = {
#     'dsn': 'https://bc53ee614b2a42bda1c6eff9127e17ca:3ee315a5d30e4d7aad1b8c2cfb893897@sentry.io/1273222',
# }
