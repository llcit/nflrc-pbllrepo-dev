from .base import *

SECRET_KEY = os.environ['SECRET_KEY']

DEBUG = True

TEMPLATE_DEBUG = True

ALLOWED_HOSTS = []

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(PROJECT_DIR.child('pbllrepo'), 'pbllrepo-dev-db.sqlite3'),
    }
}

STATIC_ROOT = '/Library/WebServer/Documents/static/pbllrepo'
STATIC_URL = '/static/'

MEDIA_ROOT = '/Library/WebServer/Documents/media/pbllrepo'
MEDIA_URL = 'http://localhost/media/pbllrepo/'

DIRECTORY = 'uploads'
FILEBROWSER_VERSIONS_BASEDIR = '_versions'

