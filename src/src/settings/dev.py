from .base import *

# https://learnwagtail.com/launch-your-wagtail-website-digital-ocean-ubuntu-18/

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = "django-insecure-=t=1$oekehhkg2fhf8^bjja116n4_5h(4_s=prtrp6q(a0#3&!"

# SECURITY WARNING: define the correct hosts in production!
ALLOWED_HOSTS = ["localhost", "*", "185.163.118.173", "dev.health4kids.de",]
CSRF_TRUSTED_ORIGINS = ["http://*.185.163.118.173"]

EMAIL_BACKEND = "django.core.mail.backends.console.EmailBackend"


try:
    from .local import *
except ImportError:
    pass
