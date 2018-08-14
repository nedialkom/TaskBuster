# -*- coding: utf-8 -*-
from .base import *

DEBUG = True

import secret_keys

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
