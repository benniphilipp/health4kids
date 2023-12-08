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

EMAIL_HOST = 'your_smtp_server'
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_HOST_USER = 'your_email@example.com'
EMAIL_HOST_PASSWORD = 'your_email_password'

try:
    from .local import *
except ImportError:
    pass
