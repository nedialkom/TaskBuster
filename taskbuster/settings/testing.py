# -*- coding: utf-8 -*-
from .base import *

DEBUG = True

import secret_keys
"""
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': secret_keys.DATABASE_NAME,
        'USER': secret_keys.DATABASE_USER,
        'PASSWORD': secret_keys.DATABASE_PASSWORD,
        'HOST': '',
        'PORT': '',
    }
}
"""

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}


FIXTURE_DIRS = [
    os.path.join(BASE_DIR, 'fixtures'),
    ]

ALLOWED_HOSTS = ['127.0.0.1']
