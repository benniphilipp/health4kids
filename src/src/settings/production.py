from .base import *

DEBUG = False

DATABASES = {
    'default': env.db(),
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'health4kids',
        'USER': 'health4kidsuser',
        'PASSWORD': 'health4kids',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}
ALLOWED_HOSTS = ["www.health4kids.de", "dev.health4kids.de", "health4kids.de", "health4kids.pixel-west.com"]
try:
    from .local import *
except ImportError:
    pass
