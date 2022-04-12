"""
Django settings for busapi project.

Generated by 'django-admin startproject' using Django 4.0.4.

For more information on this file, see
https://docs.djangoproject.com/en/4.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.0/ref/settings/
"""

import datetime
import os
from pathlib import Path
import environ
from modules.manifest import get_modules


# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.0/howto/deployment/checklist/
SETTINGS_PATH = os.path.dirname(os.path.dirname(__file__))
# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-c2kc(cgo22&2li%9ao-puy*#-@i+061jgfq!ph1uu@f15bp)zs'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ["*"]

# SITE_ID=1
# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rest_framework',
    'rest_framework.authtoken',
    'dj_rest_auth',  # 1
    'dj_rest_auth.registration',  # 2
    # 'rest_auth',
    # 'rest_auth.registration',
    'bootstrap4',
    'allauth',
    'allauth.account',
    'allauth.socialaccount',
    'allauth.socialaccount.providers.google',
    'django_extensions',
    'drf_yasg',
    'storages',
    'django_rest_passwordreset',
    'home',
    'users',
]

# LOCAL_APPS= [

# #    'feedback',
#     # 'address',
#   #   'driver',
#   #'passenger',
#  #   'allUsers',
#   #  'static'
# ]

# THIRD_PARTY_APPS= [

#     # 'allauth.socialaccount.providers.facebook',
#     # 'allauth.socialaccount.providers.apple',
# ]

# MODULES_APPS = get_modules()

# INSTALLED_APPS += LOCAL_APPS + THIRD_PARTY_APPS + MODULES_APPS 
TEMPLATE_DIRS = (
    os.path.join(SETTINGS_PATH, 'templates'),
)   
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'busapi.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'busapi.wsgi.application'


# Database
# https://docs.djangoproject.com/en/4.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': str(os.path.join(BASE_DIR, "db.sqlite3"))
    }
}
env = environ.Env()
if env.str("django.db.backends.sqlite3", default=None):
    DATABASES = {
        'default': env.db()
    }


# Password validation
# https://docs.djangoproject.com/en/4.0/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/4.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True
USE_L10N = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.0/howto/static-files/

STATIC_URL = 'static/'

# Default primary key field type
# https://docs.djangoproject.com/en/4.0/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

STATIC_ROOT = os.path.join(BASE_DIR, 'static')

MIDDLEWARE += ['whitenoise.middleware.WhiteNoiseMiddleware']

AUTHENTICATION_BACKENDS = (
    'django.contrib.auth.backends.ModelBackend',
    'allauth.account.auth_backends.AuthenticationBackend'
)

# STATIC_ROOT = os.path.join(BASE_DIR, "staticfiles")
# STATICFILES_DIRS = [os.path.join(BASE_DIR, 'static'), os.path.join(BASE_DIR, 'web_build/static')]
# STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

# allauth / users
ACCOUNT_EMAIL_REQUIRED = True
ACCOUNT_AUTHENTICATION_METHOD = 'email'
ACCOUNT_USERNAME_REQUIRED = False
ACCOUNT_EMAIL_VERIFICATION = "optional"
ACCOUNT_CONFIRM_EMAIL_ON_GET = True
ACCOUNT_LOGIN_ON_EMAIL_CONFIRMATION = True
ACCOUNT_UNIQUE_EMAIL = True
LOGIN_REDIRECT_URL = "users:redirect"

ACCOUNT_ADAPTER = "users.adapters.AccountAdapter"
SOCIALACCOUNT_ADAPTER = "users.adapters.SocialAccountAdapter"
ACCOUNT_ALLOW_REGISTRATION = env.bool("ACCOUNT_ALLOW_REGISTRATION", True)
SOCIALACCOUNT_ALLOW_REGISTRATION = env.bool("SOCIALACCOUNT_ALLOW_REGISTRATION", True)


# rest authentication #################33
REST_FRAMEWORK = {
    'DEFAULT_PERMISSION_CLASSES': (
        'rest_framework.permissions.IsAuthenticated',
    ),
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework.authentication.BasicAuthentication',
        'dj_rest_auth.jwt_auth.JWTCookieAuthentication',
        "rest_framework.authentication.TokenAuthentication",
        # to be disabled in production
        # 'rest_framework.authentication.SessionAuthentication',
    ),
    'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.LimitOffsetPagination',
    'PAGE_SIZE': 30,
    'MAX_PAGE_SIZE': 100,

}
# jwt settings########333

REST_USE_JWT = True
JWT_AUTH_COOKIE = 'auth-id'
SIMPLE_JWT = {
    'ACCESS_TOKEN_LIFETIME': datetime.timedelta(days=7),
    'REFRESH_TOKEN_LIFETIME': datetime.timedelta(days=10),
    'ROTATE_REFRESH_TOKENS': False,
    'BLACKLIST_AFTER_ROTATION': True,

    'ALGORITHM': 'HS256',
    'VERIFYING_KEY': None,
    'AUDIENCE': None,
    'ISSUER': None,

    'AUTH_HEADER_TYPES': ('Bearer',),
    'USER_ID_FIELD': 'id',
    'USER_ID_CLAIM': 'user_id',

    'AUTH_TOKEN_CLASSES': ('rest_framework_simplejwt.tokens.AccessToken',),
    'TOKEN_TYPE_CLAIM': 'token_type',

    'JTI_CLAIM': 'jti',

    'SLIDING_TOKEN_REFRESH_EXP_CLAIM': 'refresh_exp',
    'SLIDING_TOKEN_LIFETIME': datetime.timedelta(days=1),
    'SLIDING_TOKEN_REFRESH_LIFETIME': datetime.timedelta(days=3),
}

REST_AUTH_SERIALIZERS = {
    # Replace password reset serializer to fix 500 error
    "PASSWORD_RESET_SERIALIZER": "users.api.v1.serializers.PasswordSerializer",
    'USER_DETAILS_SERIALIZER': 'users.api.v1.serializers.UserDetailsSerializer',
}

REST_AUTH_REGISTER_SERIALIZERS = {
    # Use custom serializer that has no username and matches web signup
    "REGISTER_SERIALIZER": "home.api.v1.serializers.SignupSerializer",
}


# Custom user model
AUTH_USER_MODEL = "users.User"


# password reset settings ########3
DJANGO_REST_PASSWORDRESET_TOKEN_CONFIG = {
    "CLASS": "django_rest_passwordreset.tokens.RandomNumberTokenGenerator",
    "OPTIONS": {
        "min_number": 123456,
        "max_number": 999999
    }
}
DJANGO_REST_PASSWORDRESET_NO_INFORMATION_LEAKAGE = True
DJANGO_REST_MULTITOKENAUTH_RESET_TOKEN_EXPIRY_TIME = .1

EMAIL_HOST = "smtp.sendgrid.net"
EMAIL_HOST_USER = "apikey"
# EMAIL_HOST = env.str("EMAIL_HOST", "smtp.sendgrid.net")
# EMAIL_HOST_USER = env.str("SENDGRID_USERNAME", "")
# EMAIL_HOST_PASSWORD = "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"
EMAIL_HOST_PASSWORD = "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"
EMAIL_PORT = 587
EMAIL_USE_TLS = True

# DEFAULT_FROM_EMAIL = '3const.marketing@gmail.com'
# DEFAULT_TO_EMAIL = "3const.marketing@gmail.com"
# DEFAULT_INVITATION_EMAIL = "3const.marketing@gmail.com"

DEFAULT_FROM_EMAIL = "hassanafnan20@gmail.com"
DEFAULT_TO_EMAIL = "hassanafnan20@gmail.com"
DEFAULT_INVITATION_EMAIL = "hassanafnan20@gmail.com"

# # AWS S3 config
# AWS_ACCESS_KEY_ID = env.str("AWS_ACCESS_KEY_ID", "")
# AWS_SECRET_ACCESS_KEY = env.str("AWS_SECRET_ACCESS_KEY", "")
# AWS_STORAGE_BUCKET_NAME = env.str("AWS_STORAGE_BUCKET_NAME", "")
# AWS_STORAGE_REGION = env.str("AWS_STORAGE_REGION", "")

# USE_S3 = (
#     AWS_ACCESS_KEY_ID and
#     AWS_SECRET_ACCESS_KEY and
#     AWS_STORAGE_BUCKET_NAME and
#     AWS_STORAGE_REGION
# )

# if USE_S3:
#     AWS_S3_CUSTOM_DOMAIN = env.str("AWS_S3_CUSTOM_DOMAIN", "")
#     AWS_S3_OBJECT_PARAMETERS = {"CacheControl": "max-age=86400"}
#     AWS_DEFAULT_ACL = env.str("AWS_DEFAULT_ACL", "public-read")
#     AWS_MEDIA_LOCATION = env.str("AWS_MEDIA_LOCATION", "media")
#     AWS_AUTO_CREATE_BUCKET = env.bool("AWS_AUTO_CREATE_BUCKET", True)
#     DEFAULT_FILE_STORAGE = env.str(
#         "DEFAULT_FILE_STORAGE", "home.storage_backends.MediaStorage"
#     )
#     MEDIA_URL = '/mediafiles/'
#     MEDIA_ROOT = os.path.join(BASE_DIR, 'mediafiles')


# Default primary key field type
# https://docs.djangoproject.com/en/4.0/ref/settings/#default-auto-field

# DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# AUTH_USER_MODEL = "users.User"


# Swagger settings for api docs
SWAGGER_SETTINGS = {
    "DEFAULT_INFO": f"{ROOT_URLCONF}.api_info",
}