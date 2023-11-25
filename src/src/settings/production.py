from .base import *

DEBUG = False

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'health4kids',
        'USER': 'health4kidsuser',
        'PASSWORD': 'health4kids',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}

try:
    from .local import *
except ImportError:
    pass
