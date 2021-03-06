"""Production settings and globals."""


from os import environ

from memcacheify import memcacheify
from postgresify import postgresify
#from S3 import CallingFormat

from common import *

if environ.get('USE_SSLIFY'):
    MIDDLEWARE_CLASSES = ( 'sslify.middleware.SSLifyMiddleware', ) + MIDDLEWARE_CLASSES

########## DEBUG CONFIGURATION
# See: https://docs.djangoproject.com/en/dev/ref/settings/#debug
DEBUG = environ.get('DJANGO_DEBUG', False)

# See: https://docs.djangoproject.com/en/dev/ref/settings/#template-debug
TEMPLATE_DEBUG = DEBUG
########## END DEBUG CONFIGURATION


########## EMAIL CONFIGURATION
# See: https://docs.djangoproject.com/en/dev/ref/settings/#email-backend
if environ.get('USE_CELERY_EMAIL'):
    EMAIL_BACKEND = 'djcelery_email.backends.CeleryEmailBackend'

# See: https://docs.djangoproject.com/en/dev/ref/settings/#email-host
EMAIL_HOST = environ.get('EMAIL_HOST', EMAIL_HOST)

# See: https://docs.djangoproject.com/en/dev/ref/settings/#email-host-password
EMAIL_HOST_PASSWORD = environ.get('EMAIL_HOST_PASSWORD', EMAIL_HOST_PASSWORD)

# See: https://docs.djangoproject.com/en/dev/ref/settings/#email-host-user
EMAIL_HOST_USER = environ.get('EMAIL_HOST_USER', EMAIL_HOST_USER)

# See: https://docs.djangoproject.com/en/dev/ref/settings/#email-port
EMAIL_PORT = environ.get('EMAIL_PORT', EMAIL_PORT)

# See: https://docs.djangoproject.com/en/dev/ref/settings/#email-subject-prefix
EMAIL_SUBJECT_PREFIX = '[{0}] '.format(SITE_NAME)

# See: https://docs.djangoproject.com/en/dev/ref/settings/#email-use-tls
EMAIL_USE_TLS = True

# See: https://docs.djangoproject.com/en/dev/ref/settings/#server-email
SERVER_EMAIL = EMAIL_HOST_USER
########## END EMAIL CONFIGURATION


########## DATABASE CONFIGURATION
DATABASES = postgresify()
########## END DATABASE CONFIGURATION


########## CACHE CONFIGURATION
# See: https://docs.djangoproject.com/en/dev/ref/settings/#caches
CACHES = memcacheify()
########## END CACHE CONFIGURATION


########## CELERY CONFIGURATION
# See: http://docs.celeryproject.org/en/latest/configuration.html#broker-transport
BROKER_TRANSPORT = 'amqplib'

# Set this number to the amount of allowed concurrent connections on your AMQP
# provider, divided by the amount of active workers you have.
#
# For example, if you have the 'Little Lemur' CloudAMQP plan (their free tier),
# they allow 3 concurrent connections. So if you run a single worker, you'd
# want this number to be 3. If you had 3 workers running, you'd lower this
# number to 1, since 3 workers each maintaining one open connection = 3
# connections total.
#
# See: http://docs.celeryproject.org/en/latest/configuration.html#broker-pool-limit
try:
    BROKER_POOL_LIMIT = int(environ.get('BROKER_POOL_LIMIT', 1))
except Exception:
    BROKER_POOL_LIMIT = 1

# See: http://docs.celeryproject.org/en/latest/configuration.html#broker-connection-max-retries
BROKER_CONNECTION_MAX_RETRIES = 0

# See: http://docs.celeryproject.org/en/latest/configuration.html#broker-url
BROKER_URL = environ.get('RABBITMQ_URL') or environ.get('CLOUDAMQP_URL')

# See: http://docs.celeryproject.org/en/latest/configuration.html#celery-result-backend
# This might create Error loop if Connection Error occurs while establishing connection to ampq
# Another solution could be to use a backend other than ampq
#CELERY_RESULT_BACKEND = 'amqp'

# Modules to import and register tasks
CELERY_IMPORTS = ['libs.periodic_tasks']

CELERY_EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
########## END CELERY CONFIGURATION


########## STORAGE CONFIGURATION
# See: http://django-storages.readthedocs.org/en/latest/index.html
INSTALLED_APPS += (
    'storages',
    'raven.contrib.django.raven_compat',    # Sentry
    'djcelery_email',
)

# See: http://django-storages.readthedocs.org/en/latest/backends/amazon-S3.html#settings
STATICFILES_STORAGE = 'libs.s3.HerokuStaticS3BotoStorage'
DEFAULT_FILE_STORAGE = 'storages.backends.s3boto.S3BotoStorage'

# See: http://django-storages.readthedocs.org/en/latest/backends/amazon-S3.html#settings
#AWS_CALLING_FORMAT = CallingFormat.SUBDOMAIN

# See: http://django-storages.readthedocs.org/en/latest/backends/amazon-S3.html#settings
AWS_ACCESS_KEY_ID = environ.get('AWS_ACCESS_KEY_ID', '')
AWS_SECRET_ACCESS_KEY = environ.get('AWS_SECRET_ACCESS_KEY', '')
AWS_STORAGE_BUCKET_NAME = environ.get('AWS_STORAGE_BUCKET_NAME', '')
AWS_STATIC_STORAGE_BUCKET_NAME = environ.get('AWS_STATIC_STORAGE_BUCKET_NAME', '')
AWS_AUTO_CREATE_BUCKET = False
AWS_QUERYSTRING_AUTH = False

# AWS cache settings, don't change unless you know what you're doing:
AWS_EXPIRY = 60 * 60 * 24 * 7
AWS_HEADERS = {
    'Cache-Control': 'max-age=%d, s-maxage=%d, must-revalidate' % (AWS_EXPIRY,
        AWS_EXPIRY)
}

# See: https://docs.djangoproject.com/en/dev/ref/settings/#static-url
STATIC_URL = 'https://s3.amazonaws.com/{0}/'.format(AWS_STATIC_STORAGE_BUCKET_NAME)

MEDIA_URL = 'https://s3.amazonaws.com/{0}/'.format(AWS_STORAGE_BUCKET_NAME)
########## END STORAGE CONFIGURATION


########## COMPRESSION CONFIGURATION
# See: http://django_compressor.readthedocs.org/en/latest/settings/#django.conf.settings.COMPRESS_OFFLINE
COMPRESS_OFFLINE = True

COMPRESS_CSS_FILTERS = [
# 'compressor.filters.css_default.CssAbsoluteFilter',
'libs.compress_filters.HerokuCssAbsoluteFilter'
]

# See: http://django_compressor.readthedocs.org/en/latest/settings/#django.conf.settings.COMPRESS_CSS_FILTERS
#COMPRESS_CSS_FILTERS += [
#    'compressor.filters.cssmin.CSSMinFilter',
#]

# See: http://django_compressor.readthedocs.org/en/latest/settings/#django.conf.settings.COMPRESS_JS_FILTERS
#COMPRESS_JS_FILTERS += [
#    'compressor.filters.jsmin.JSMinFilter',
#]
########## END COMPRESSION CONFIGURATION


########## SECRET CONFIGURATION
# See: https://docs.djangoproject.com/en/dev/ref/settings/#secret-key
SECRET_KEY = environ.get('SECRET_KEY', SECRET_KEY)
########## END SECRET CONFIGURATION

########## ALLOWED HOSTS CONFIGURATION
# See: https://docs.djangoproject.com/en/dev/ref/settings/#allowed-hosts
ALLOWED_HOSTS = ['.herokuapp.com']
########## END ALLOWED HOST CONFIGURATION


########## HTTPS CONFIGURATION
# Honor the 'X-Forwarded-Proto' header for request.is_secure()
# Heroku uses this : https://devcenter.heroku.com/articles/http-routing#heroku-headers
SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')
########## ENDS HTTPS CONFIGURATION


########## SENTRY
RAVEN_CONFIG = {
    'dsn': environ.get('SENTRY_DSN'),
}
########## END SENTRY


########## MICS
# Robots.txt
ALLOW_SEARCH_ENGINE_INDEXING = environ.get('ALLOW_SEARCH_ENGINE_INDEXING', True)

#Disable static urls
EXPOSE_STATIC_URLS = environ.get('EXPOSE_STATIC_URLS', False)
########## END MISC


########## DEPENDANT SETTINGS
COMPRESS_URL = STATIC_URL

# See: http://django_compressor.readthedocs.org/en/latest/settings/#django.conf.settings.COMPRESS_STORAGE
COMPRESS_STORAGE = STATICFILES_STORAGE
THUMBNAIL_DEFAULT_STORAGE = DEFAULT_FILE_STORAGE
########## END DEPENDANT SETTINGS
