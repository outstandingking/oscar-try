# -*- coding:utf-8 -*-
"""
Django settings for frobshop project.

Generated by 'django-admin startproject' using Django 1.10.7.

For more information on this file, see
https://docs.djangoproject.com/en/1.10/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.10/ref/settings/
"""

import os
from oscar.defaults import *
from oscar import get_core_apps

from os.path import join, dirname, abspath

from oscar import OSCAR_MAIN_TEMPLATE_DIR

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
# POSTSQL_CONN = os.environ.get('POSTSQL_CONN',None)

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.10/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'fc+*f%-2uv4f*)b-&_70qtb*)pi#537ept72@t2392(e506y5f'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = [
    '0.0.0.0',
    '127.0.0.1',
    'localhost',
    '*'
]


QINIU_ACCESS_KEY = '-4_KxRQslAjfSYpEaCkbFXAd792TINkUFzUCHOdE'
QINIU_SECRET_KEY = '3Ehh1CN2PIEXNSeivFevSLBE3PzO3evo_UwdOckc'
QINIU_BUCKET_NAME = 'oscar'
QINIU_BUCKET_DOMAIN = 'ox8265im3.bkt.clouddn.com/'
QINIU_SECURE_URL = False      #使用http


PREFIX_URL = 'http://'

MEDIA_URL = PREFIX_URL + QINIU_BUCKET_DOMAIN  + '/media/'
MEDIA_ROOT = 'media'

THUMBNAIL_DEBUG=True
DEFAULT_FILE_STORAGE = 'qiniustorage.backends.QiniuMediaStorage'

REST_FRAMEWORK = {

    'DATETIME_FORMAT': "%m/%d/%Y %H:%M:%S",
    'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.PageNumberPagination',
    'PAGE_SIZE': 20

}
# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.flatpages',
    'django.contrib.sites',
    'widget_tweaks',
    'compressor',
    'rest_framework',
    'rest_framework.authtoken',
    'UserInfo',
    'ProductInfo',
    'senderConfirmInfo'

                 ]+ get_core_apps([])


SITE_ID = 1

MIDDLEWARE_CLASSES = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'oscar.apps.basket.middleware.BasketMiddleware',

]

AUTHENTICATION_BACKENDS = (
    'oscar.apps.customer.auth_backends.EmailBackend',
    'django.contrib.auth.backends.ModelBackend',
    # 'rest_framework.permissions.IsAuthenticated',
#
)

ROOT_URLCONF = 'frobshop.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS':[
            os.path.join(BASE_DIR, 'templates'),
            OSCAR_MAIN_TEMPLATE_DIR
        ],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',


                'oscar.apps.search.context_processors.search_form',
                'oscar.apps.promotions.context_processors.promotions',
                'oscar.apps.checkout.context_processors.checkout',
                'oscar.apps.customer.notifications.context_processors.notifications',
                'oscar.core.context_processors.metadata',
            ],
        },
    },
]
OSCAR_DEFAULT_CURRENCY = 'GBP'

WSGI_APPLICATION = 'frobshop.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.10/ref/settings/#databases
DATABASES = {

    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'postgres',
        'USER': 'postgres',
        'PASSWORD': '',
        'HOST': '127.0.0.1',
        'PORT': '5432',
    }
}


HAYSTACK_CONNECTIONS = {
    'default': {
        'ENGINE': 'haystack.backends.simple_backend.SimpleEngine',
    },
}

# MEDIA_URL = '/media/'
# MEDIA_ROOT = 'media/'
STATIC_URL = PREFIX_URL + QINIU_BUCKET_DOMAIN+ '/static/'

STATIC_ROOT = '/static/'
STATICFILES_STORAGE = 'qiniustorage.backends.QiniuStaticStorage'
# Password validation
# https://docs.djangoproject.com/en/1.10/ref/settings/#auth-password-validators

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

FILE_UPLOAD_HANDLERS = [
    'django.core.files.uploadhandler.MemoryFileUploadHandler',
    'django.core.files.uploadhandler.TemporaryFileUploadHandler',
]
# Internationalization
# https://docs.djangoproject.com/en/1.10/topics/i18n/
OSCAR_FROM_EMAIL = 'test@gmail.com'

EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

OSCAR_ORDER_STATUS_PIPELINE ={
    'Pending': ('Being processed', 'Cancelled',),
    'Being processed': ('Processed', 'Cancelled',),
    'Cancelled': (),
    }


OSCAR_DEFAULT_CURRENCY = '¥'
LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


IMAGES = "images-all"
Images_DEFAULT = join(IMAGES, "default-avatar.png")

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.10/howto/static-files/



