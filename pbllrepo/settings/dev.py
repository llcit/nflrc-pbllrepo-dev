from .base import *

SECRET_KEY = os.environ['SECRET_KEY']

DEBUG = True

ALLOWED_HOSTS = ['clt.developers.edu']

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'nflrc-pbllrepo-dev-db',
        'USER': 'postgres',
        'PASSWORD': '1',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}

MEDIA_URL = 'http://localhost/media/pbllrepo/'
MEDIA_ROOT = '/Library/WebServer/Documents/media/pbllrepo'

STATIC_ROOT = '/Library/WebServer/Documents/static/pbllrepo'
STATIC_URL = '/static/'

DIRECTORY = 'uploads'
FILEBROWSER_VERSIONS_BASEDIR = '_versions'

SOCIAL_AUTH_GOOGLE_OAUTH2_SECRET = os.environ['SOCIAL_AUTH_GOOGLE_OAUTH2_SECRET']
SOCIAL_AUTH_GOOGLE_OAUTH2_KEY = os.environ['SOCIAL_AUTH_GOOGLE_OAUTH2_KEY']  # This is the Client ID (not a key)

SOCIAL_AUTH_PIPELINE = (
    'social_core.pipeline.social_auth.social_details',
    'social_core.pipeline.social_auth.social_uid',

    'core.utils.nflrc_auth_allowed',
    # 'core.utils.nflrc_social_user',

    'social_core.pipeline.user.get_username',
    'social_core.pipeline.social_auth.associate_user',
    'social_core.pipeline.social_auth.load_extra_data',
    'social_core.pipeline.user.user_details',
)

LOGIN_URL = '/login/google-oauth2/'
LOGIN_REDIRECT_URL = '/'

HAYSTACK_CONNECTIONS = {
    'default': {
        'ENGINE': 'haystack.backends.whoosh_backend.WhooshEngine',
        'PATH': os.environ['WHOOSH_PATH'],
    },
}
