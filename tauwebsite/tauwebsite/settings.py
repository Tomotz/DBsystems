"""
Django settings for tauwebsite project.

Generated by 'django-admin startproject' using Django 1.11.dev20170115123718.

For more information on this file, see
https://docs.djangoproject.com/en/dev/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/dev/ref/settings/
"""

import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/dev/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '^kiwo*llkg$xd#qoi7t6$@5ynweuyap@lb05pi!j6gha#^e2&x'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    'places.apps.PlacesConfig',
    'users.apps.UsersConfig',
    #'django.contrib.admin',
    #'django.contrib.auth',
    #'django.contrib.contenttypes',
    #'django.contrib.sessions',
    #'django.contrib.messages',
    'django.contrib.staticfiles',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'tauwebsite.urls'

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

WSGI_APPLICATION = 'tauwebsite.wsgi.application'


LOCAL_DB_PASS = os.environ.get('LOCAL_DB_PASS')

# Django DB configuration ---UNUSED---
# https://docs.djangoproject.com/en/dev/ref/settings/#databases
DATABASES = {
    #'default': {
    #    'ENGINE': 'django.db.backends.mysql',
    #    'NAME': 'DbMysql17',
    #    'USER': 'root',
    #    'PASSWORD': LOCAL_DB_PASS,
    #    'HOST': 'localhost',
    #    'PORT': '3306'
    #}
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'DbMysql17',
        'USER': 'DbMysql17',
        'PASSWORD': 'DbMysql17',
        'HOST': 'mysqlsrv.cs.tau.ac.il',
        'PORT': '3306'
    }
}

# Manual DB connection, in use
import MySQLdb as mdb
DB_CONN = mdb.connect(DATABASES['default']['HOST'], DATABASES['default']['USER'], DATABASES['default']['PASSWORD'], DATABASES['default']['NAME'], port=int(DATABASES['default']['PORT']), use_unicode=True, charset="utf8")
# DB_CONN = mdb.connect("127.0.0.1", "root", LOCAL_DB_PASS, "DbMysql17", port=3306, use_unicode=True, charset="utf8")

LOGGING = {
    'version': 1,
    'handlers': {
        'console':{
            'level':'DEBUG',
            'class':'logging.StreamHandler',
        },
    },
    'loggers': {
        'django.request': {
            'handlers':['console'],
            'propagate': True,
            'level':'DEBUG',
        }
    },
}
# Password validation
# https://docs.djangoproject.com/en/dev/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/dev/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/dev/howto/static-files/

STATIC_URL = '/static/'
STATIC_FILES_FULL_PATH = os.environ.get('DBMS_PATH')
# STATIC_FILES_FULL_PATH = r"C:\Users\liadwg\Desktop\liad\CS\DBMS APP\DBsystems\app",

STATICFILES_DIRS = (
    STATIC_FILES_FULL_PATH,
)
