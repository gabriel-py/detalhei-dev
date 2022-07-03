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
    DEFAULT_AUTO_FIELD,
    BASE_DIR,
    AUTH_USER_MODEL,
    REST_FRAMEWORK,
    SIMPLE_JWT,
    DJOSER,
    AUTHENTICATION_BACKENDS,
    SOCIAL_AUTH_GOOGLE_OAUTH2_KEY,
    SOCIAL_AUTH_GOOGLE_OAUTH2_SECRET,
    SOCIAL_AUTH_GOOGLE_OAUTH2_SCOPE,
    SOCIAL_AUTH_GOOGLE_OAUTH2_EXTRA_DATA
)

ALLOWED_HOSTS = [
    'localhost',
    '127.0.0.1'
]

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

# INSTALLED_APPS += [
#     'django_extensions'
# ]