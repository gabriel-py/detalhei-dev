from decouple import config
import os
from .base import (
    STATIC_ROOT,
    STATIC_URL,
    MEDIA_URL,
    MEDIA_ROOT,
    DEBUG,
    SECRET_KEY,
    LANGUAGE_CODE,
    TIME_ZONE,
    USE_I18N,
    USE_TZ,
    INSTALLED_APPS,
    ROOT_URLCONF,
    AUTH_PASSWORD_VALIDATORS,
    MIDDLEWARE,
    TEMPLATES,
    DEFAULT_AUTO_FIELD
)

ALLOWED_HOSTS = [
    'localhost',
    '127.0.0.1'
]

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': config('DBNAME'),
        'USER': config('DBUSER'),
        'PASSWORD': config('DBPASSWORD'),
        'HOST': config('DBHOST')
    }
}