from .base import *

DEBUG = False

DATABASES = {
    'default': env.db(),

}
ALLOWED_HOSTS = ["www.health4kids.de", "dev.health4kids.de", "health4kids.de", "health4kids.pixel-west.com"]
try:
    from .local import *
except ImportError:
    pass