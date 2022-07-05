from pathlib import Path
from decouple import config
import os

BASE_DIR = Path(__file__).resolve().parent.parent.parent
STATIC_ROOT = BASE_DIR / 'static'
STATIC_URL = 'static/'

MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media'

DEBUG = config("DEBUG", cast=bool)
SECRET_KEY = config('SECRET_KEY')

LANGUAGE_CODE = 'pt-br'
TIME_ZONE = 'America/Sao_Paulo'
USE_I18N = True
USE_TZ = True


INSTALLED_APPS = [
    'src.django_stisla.apps.admin',
    "django.contrib.admin",
    "django.contrib.auth",
    'widget_tweaks',
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",

    # LIBS
    # 'nested_admin',
    # 'rest_framework',
    # 'rest_framework.authtoken',
    # 'drf_yasg',
    # 'core',
    'rest_framework',
    'rest_framework.authtoken',
    'djoser',
    'social_django',
    'src.usuarios.apps.UsuariosConfig',
    'src.produto.apps.ProdutoConfig'
]

ROOT_URLCONF = "src.urls"

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
    },
]

MIDDLEWARE = [
    'social_django.middleware.SocialAuthExceptionMiddleware',
    # "corsheaders.middleware.CorsMiddleware",
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [BASE_DIR / 'templates'],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
                'django.template.context_processors.request',

                'social_django.context_processors.backends',
                'social_django.context_processors.login_redirect'
            ],
        },
    },
]

WSGI_APPLICATION = "src.wsgi.application"
DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

AUTH_USER_MODEL = 'usuarios.UserAccount'

AUTHENTICATION_BACKENDS = (
    'social_core.backends.google.GoogleOAuth2',
    'social_core.backends.facebook.FacebookOAuth2',
    'social_core.backends.twitter.TwitterOAuth',
    'django.contrib.auth.backends.ModelBackend'
)

REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': (
        # 'rest_framework.authentication.TokenAuthentication',
        'rest_framework_simplejwt.authentication.JWTAuthentication',
        # 'rest_framework_simplejwt.authentication.JSONWebTokenAuthentication',
    ),
     'DEFAULT_PERMISSION_CLASSES': (
         'rest_framework.permissions.IsAuthenticated',
        ),
}

SIMPLE_JWT = {
   'AUTH_HEADER_TYPES': ('JWT',),
#    'AUTH_HEADER_TYPES': ('Baerer',),
    # 'AUTH_TOKEN_CLASSES': (
    #     'rest_framework_simplejwt.tokens.AccessToken',
    # ),
    # 'USER_AUTHENTICATION_RULE': 'rest_framework_simplejwt.authentication.default_user_authentication_rule',
}

DJOSER = {
    'LOGIN_FIELD': 'email',
    'USER_CREATE_PASSWORD_RETYPE': True,
    'USERNAME_CHANGED_EMAIL_CONFIRMATION': True,
    'PASSWORD_CHANGED_EMAIL_CONFIRMATION': True,
    'SEND_CONFIRMATION_EMAIL': True,
    'SET_USERNAME_RETYPE': True,
    'SET_PASSWORD_RETYPE': True,
    'PASSWORD_RESET_CONFIRM_URL': 'password/reset/confirm/{uid}/{token}',
    'USERNAME_RESET_CONFIRM_URL': 'email/reset/confirm/{uid}/{token}',
    'ACTIVATION_URL': 'activate/{uid}/{token}',
    'SEND_ACTIVATION_EMAIL': True,
    'SOCIAL_AUTH_TOKEN_STRATEGY': 'djoser.social.token.jwt.TokenStrategy',
    'SOCIAL_AUTH_ALLOWED_REDIRECT_URIS': [
        'http://localhost:8000/google',
        'http://localhost:8000/facebook',
        'http://127.0.0.1:8000/complete/twitter'
    ],
    'SERIALIZERS': {
        'user_create': 'src.usuarios.serializers.UserCreateSerializer',
        'user': 'src.usuarios.serializers.UserCreateSerializer',
        'current_user': 'src.usuarios.serializers.UserCreateSerializer',
        'user_delete': 'djoser.serializers.UserDeleteSerializer',
    }
}

SOCIAL_AUTH_GOOGLE_OAUTH2_KEY = '121052205608-f4s21166k542p2l6rb2vgsjl31fhd419.apps.googleusercontent.com'
SOCIAL_AUTH_GOOGLE_OAUTH2_SECRET = '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'
SOCIAL_AUTH_GOOGLE_OAUTH2_SCOPE = [
    'https://www.googleapis.com/auth/userinfo.email',
    'https://www.googleapis.com/auth/userinfo.profile',
    'openid'
]
SOCIAL_AUTH_GOOGLE_OAUTH2_EXTRA_DATA = [
    'first_name',
    'last_name'
]

SOCIAL_AUTH_FACEBOOK_KEY = '414951983981584'
SOCIAL_AUTH_FACEBOOK_SECRET = '36c1fbc78eaa638e27d8784fa93ef173'
SOCIAL_AUTH_FACEBOOK_SCOPE = ['email']
SOCIAL_AUTH_FACEBOOK_PROFILE_EXTRA_PARAMS = {
    'fields': 'email, first_name, last_name'
}

SOCIAL_AUTH_TWITTER_KEY = 'YoaT5yecJWFTnEbxIZz8d4Plz'
# SOCIAL_AUTH_TWITTER_KEY = 'WnlVWUgzWVRmUDV0QldLYWpwVzI6MTpjaQ'
SOCIAL_AUTH_TWITTER_SECRET = 'YI63WvSsLaUBxWw6Xogv46lO8drjXEdeU2D6bccfBtmtKvhUip'
# SOCIAL_AUTH_TWITTER_SECRET = '40YC34xbh6Vm5p2cM089TbNtD2bhCVji6e1x6CCsDoKhcRREqi'
BAERER='AAAAAAAAAAAAAAAAAAAAABC5eQEAAAAAvtZMyGKIpq1Bkaa%2BGINjFEgZmy4%3DOjm6KOhrHdAK7S3UeJK0FBKGZXOKms2hl0FKaecrv87j47lu9V'