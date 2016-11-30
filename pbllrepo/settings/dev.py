from .base import *

SECRET_KEY = os.environ['SECRET_KEY']

DEBUG = True

TEMPLATE_DEBUG = True

ALLOWED_HOSTS = []

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'nflrc-pbllrepo-dev-db',
        'USER': 'postgres',
        'PASSWORD': '1',
        'HOST': 'localhost',
        'PORT': '5432',
    }

    # 'default': {
    #     'ENGINE': 'django.db.backends.sqlite3',
    #     'NAME': os.path.join(PROJECT_DIR.child('pbllrepo'), 'pbllrepo-dev-sample.sqlite3'),
    # }
}



STATIC_ROOT = '/Library/WebServer/Documents/static/pbllrepo'
STATIC_URL = '/static/'

MEDIA_ROOT = '/Library/WebServer/Documents/media/pbllrepo'
MEDIA_URL = 'http://localhost/media/pbllrepo/'

DIRECTORY = 'uploads'
FILEBROWSER_VERSIONS_BASEDIR = '_versions'

SOCIAL_AUTH_GOOGLE_OAUTH2_SECRET = os.environ['SOCIAL_AUTH_GOOGLE_OAUTH2_SECRET']
SOCIAL_AUTH_GOOGLE_OAUTH2_KEY = os.environ['SOCIAL_AUTH_GOOGLE_OAUTH2_KEY']  # This is the Client ID (not a key)

SOCIAL_AUTH_PIPELINE = (
    'social.pipeline.social_auth.social_details',
    'social.pipeline.social_auth.social_uid',

    'core.utils.nflrc_auth_allowed',
    # 'core.utils.nflrc_social_user',

    'social.pipeline.user.get_username',
    'social.pipeline.social_auth.associate_user',
    'social.pipeline.social_auth.load_extra_data',
    'social.pipeline.user.user_details',
)

LOGIN_URL = '/login/google-oauth2/'
LOGIN_REDIRECT_URL = '/'
