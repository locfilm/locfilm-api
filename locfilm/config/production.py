import os
from .common import Common

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


class Production(Common):
    INSTALLED_APPS = Common.INSTALLED_APPS
    SECRET_KEY = os.getenv('DJANGO_SECRET_KEY')
    # Site
    # https://docs.djangoproject.com/en/2.0/ref/settings/#allowed-hosts
    ALLOWED_HOSTS = ["*"]
    INSTALLED_APPS += ("gunicorn", )

    # Static files (CSS, JavaScript, Images)
    # https://docs.djangoproject.com/en/2.0/howto/static-files/
    # http://django-storages.readthedocs.org/en/latest/index.html
    INSTALLED_APPS += ('storages',)
    # Media files
    AWS_LOCATION = 'static'

    AWS_ACCESS_KEY_ID = os.getenv('DJANGO_AWS_ACCESS_KEY_ID')
    AWS_SECRET_ACCESS_KEY = os.getenv('DJANGO_AWS_SECRET_ACCESS_KEY')
    AWS_STORAGE_BUCKET_NAME = os.getenv('DJANGO_AWS_STORAGE_BUCKET_NAME')

    AWS_S3_CUSTOM_DOMAIN = '%s.s3.amazonaws.com' % AWS_STORAGE_BUCKET_NAME
    AWS_S3_OBJECT_PARAMETERS = {
        'CacheControl': 'max-age=86400',
    }
    AWS_QUERYSTRING_AUTH = False
    AWS_DEFAULT_ACL = None
    STATICFILES_DIRS = [str(os.path.dirname("static"))]

    STATICFILES_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'  #
    DEFAULT_FILE_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'

    AWS_AUTO_CREATE_BUCKET = True
    AWS_QUERYSTRING_AUTH = False
    MEDIA_URL = f'https://s3.amazonaws.com/{AWS_STORAGE_BUCKET_NAME}/'

    # Static files (CSS, JavaScript, Images)
    # https://docs.djangoproject.com/en/2.0/howto/static-files/
    STATIC_URL = 'https://%s/%s/' % (AWS_S3_CUSTOM_DOMAIN, AWS_LOCATION)

    ADMIN_MEDIA_PREFIX = STATIC_URL + 'admin/'

    MEDIA_ROOT = 'https://%s/%s/media' % (AWS_S3_CUSTOM_DOMAIN, AWS_LOCATION)
    STATIC_ROOT = os.path.normpath(os.path.join(os.path.dirname(BASE_DIR), 'static'))
    STATICFILES_DIRS = []
    STATICFILES_FINDERS = (
        'django.contrib.staticfiles.finders.FileSystemFinder',
        'django.contrib.staticfiles.finders.AppDirectoriesFinder',
    )

    # https://developers.google.com/web/fundamentals/performance/optimizing-content-efficiency/http-caching#cache-control
    # Response can be cached by browser and any intermediary caches (i.e. it is "public") for up to 1 day
    # 86400 = (60 seconds x 60 minutes x 24 hours)
    AWS_HEADERS = {
        'Cache-Control': 'max-age=86400, s-maxage=86400, must-revalidate',
    }
