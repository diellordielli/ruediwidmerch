import os
import sys
import dj_database_url

WEBAPP_DIR = os.path.dirname(os.path.abspath(__file__))
APP_BASEDIR = os.path.abspath(os.path.join(WEBAPP_DIR, os.path.pardir))

DEBUG = os.getenv('DEBUG_MODE', 'true') == 'true'
TEMPLATE_DEBUG = DEBUG

ALLOWED_HOSTS = ['localhost', '.herokuapp.com', '.heroku.feinheit.ch']

ADMINS = (
    ('FEINHEIT Developers', 'dev@feinheit.ch'),
)

MANAGERS = ADMINS

SECRET_KEY = os.environ.get('SECRET_KEY', 'mbwzi$440)f6j_*q*5#@8el#)3gs4jl*$^6yo1@8y5qs^2535x')

# Parse database configuration from $DATABASE_URL
DEV_DB = os.path.join(APP_BASEDIR, 'dev.db')
DATABASES = {'default': dj_database_url.config(default='sqlite:///%s' % DEV_DB)}

# Honor the 'X-Forwarded-Proto' header for request.is_secure()
SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')

TIME_ZONE = 'Europe/Zurich'

_ = lambda s: s

LANGUAGE_CODE = 'de'

LANGUAGES = (
    ('de', _('German')),
    ('en', _('English')),
    ('fr', _('French')),
    ('it', _('Italian')),
)

SITE_ID = 1

USE_I18N = True
USE_L10N = True
USE_TZ = True

AWS_ACCESS_KEY_ID = os.environ.get('AWS_ACCESS_KEY_ID', '')
AWS_SECRET_ACCESS_KEY = os.environ.get('AWS_SECRET_ACCESS_KEY', '')
AWS_STORAGE_BUCKET_NAME = os.environ.get('AWS_STORAGE_BUCKET_NAME', '')

MEDIA_ROOT = os.path.join(APP_BASEDIR, 'uploads')
MEDIA_URL = '/uploads/'

if 'runserver' not in sys.argv:
    DEFAULT_FILE_STORAGE = 'storages.backends.s3boto.S3BotoStorage'

STATIC_ROOT = os.path.join(APP_BASEDIR, 'static')
STATIC_URL = '/static/'

STATICFILES_DIRS = (os.path.join(WEBAPP_DIR, 'static'),)

ROOT_URLCONF = 'ruediwidmerch.urls'

if 'runserver' in sys.argv:
    EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
else:
    EMAIL_HOST = 'smtp.sendgrid.net'
    EMAIL_HOST_USER = os.environ.get('SENDGRID_USERNAME', '')
    EMAIL_HOST_PASSWORD = os.environ.get('SENDGRID_PASSWORD', '')
    EMAIL_PORT = 587
    EMAIL_USE_TLS = True


DEFAULT_FROM_EMAIL = os.getenv('DEFAULT_FROM_EMAIL', 'root@oekohosting.ch')
SERVER_EMAIL = os.getenv('DEFAULT_FROM_EMAIL', 'root@oekohosting.ch')

TEMPLATE_DIRS = (
    os.path.join(WEBAPP_DIR, 'templates')
)

TEMPLATE_CONTEXT_PROCESSORS = (
    'django.contrib.auth.context_processors.auth',
    'django.core.context_processors.debug',
    'django.core.context_processors.i18n',
    'django.core.context_processors.media',
    'django.core.context_processors.static',
    'django.core.context_processors.request',
    'django.contrib.messages.context_processors.messages',
    'ruediwidmerch.context_processors.feincms_pages',
    'ruediwidmerch.context_processors.config',
)

INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.admin',
    'django.contrib.admindocs',

    'raven.contrib.django.raven_compat',
    'storages',
    'fhadmin',
    'tinymce',
    'south',
    'mptt',

    'feincms',
    'feincms.module.page',
    'feincms.module.medialibrary',
    'feincms_oembed',

    #'elephantblog',

    'ruediwidmerch',
)

from memcacheify import memcacheify

CACHES = memcacheify()

SESSION_ENGINE = 'django.contrib.sessions.backends.cached_db'


from fhadmin import FHADMIN_GROUPS_REMAINING
_ = lambda x: x

FHADMIN_GROUPS_CONFIG = [
    (_('Content'), {
        'apps': ('page', 'medialibrary'),
    }),
    (_('Others'), {
        'apps': (FHADMIN_GROUPS_REMAINING),
    }),
    (_('Settings and users'), {
        'apps': ('sites', 'auth'),
    }),

]

FEINCMS_RICHTEXT_INIT_CONTEXT = {
    'TINYMCE_JS_URL': '/static/tiny_mce/tiny_mce.js',
}

SOUTH_MIGRATION_MODULES = dict((app, 'ruediwidmerch.migrate.%s' % app) for app in (
    'medialibrary',
    'page',
    'elephantblog',
))

GA_CODE = os.getenv('GA_CODE', '')


# def elephantblog_entry_url_app(self):
#     from feincms.content.application.models import app_reverse
#     return app_reverse('elephantblog_entry_detail', 'elephantblog.urls', kwargs={
#         'year': self.published_on.strftime('%Y'),
#         'month': self.published_on.strftime('%m'),
#         'day': self.published_on.strftime('%d'),
#         'slug': self.slug,
#     })


# def elephantblog_categorytranslation_url_app(self):
#     from feincms.content.application.models import app_reverse
#     return app_reverse('elephantblog_category_detail', 'elephantblog.urls', kwargs={
#         'slug': self.slug,
#     })

# ABSOLUTE_URL_OVERRIDES = {
#     'elephantblog.entry': elephantblog_entry_url_app,
#     'elephantblog.categorytranslation': elephantblog_categorytranslation_url_app,
# }
