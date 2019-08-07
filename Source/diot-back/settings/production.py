from .base import *


TEMPLATE_LOADERS = (
    ('django.template.loaders.cached.Loader', (
        'django.template.loaders.filesystem.Loader',
        'django.template.loaders.app_directories.Loader',
    )),
)

try:
    from .local import *
except ImportError:
    pass

STATIC_URL = 'http://167.99.106.240:8000/static/'
