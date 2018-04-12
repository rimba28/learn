﻿"""
Django settings for N_Asset project.

Generated by 'django-admin startproject' using Django 1.9.1.

For more information on this file, see
https://docs.djangoproject.com/en/1.9/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.9/ref/settings/
"""

import os
import posixpath

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.9/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'b9578a94-76ea-4936-8cfe-94b039a639ef'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

INTERNAL_IPS = ('127.0.0.1', 'localhost',)

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    'app',
	'NA_DataLayer',
	'NA_Domain',
	'NA_Models',
    'NA_DataLayer.NA_User',
    # Add your apps here to enable them
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    #'debug_toolbar',
    #'clear_cache',
]

#SESSION_ENGINE = "django.contrib.sessions.backends.cache"
#SESSION_CACHE_ALIAS = "default"

MIDDLEWARE_CLASSES = [
    #'django.middleware.cache.UpdateCacheMiddleware',
    #'debug_toolbar.middleware.DebugToolbarMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'app.middleware.GlobalUserMiddleware', #access user as Global scope for log event and another using signal built-in django, because the signal such as models they can't get request from HTTP 
    #'django.middleware.cache.FetchFromCacheMiddleware',
]

ROOT_URLCONF = 'N_Asset.urls'

AUTH_USER_MODEL = 'NA_User.User'

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

WSGI_APPLICATION = 'N_Asset.wsgi.application'


# Database

DATABASES = {
      'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'na_m_s',
        'USER': 'root',
        'PASSWORD': '',
        'HOST': 'localhost',
        'PORT': '3306',
		}
}


# Password validation
# https://docs.djangoproject.com/en/1.9/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/1.9/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'Asia/Jakarta' #datetime Jakarta

USE_I18N = True

USE_L10N = True

USE_TZ = False

DATETIME_FORMAT = [
    '%Y-%m-%d %H:%M:%S'
    ]

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.9/howto/static-files/

STATIC_URL = '/static/'

STATIC_ROOT = posixpath.join(*(BASE_DIR.split(os.path.sep) + ['app/static']))

MEDIA_URL = os.path.join(BASE_DIR, 'app/static/NA_User_Image/img/')

MEDIA_ROOT = os.path.join(BASE_DIR, 'app/static/NA_User_Image/UploadImg/')

from django.core.urlresolvers import reverse_lazy
LOGIN_URL = reverse_lazy('login') #this for custom login url e.g: localhost:8000/login?=next/ and the default url is localhost:8000/account?=next .. . :D


#STATICFILES_STORAGE = 'django.contrib.staticfiles.storage.CachedStaticFilesStorage'

#This is Rimba's branch
#This is Rimba's branch and another changes
#This is Rimba's branch
#This is Rimba's branch and another changes
#This is Rimba's branch
#This is Rimba's branch and another changes
#This is Rimba's branch
#This is Rimba's branch and another changes

#This is digabungkeun .. .:D

#Ok This is original
#This is Rimba's branch
#Ok This is original
#This is Rimba's branch
#Ok This is original
#This is Rimba's branch
#Ok This is original

EMAIL_USE_TLS=True
EMAIL_BACKEND='django.core.mail.backends.console.EmailBackend'
EMAIL_HOST='smtp.gmail.com'
EMAIL_PORT=587
EMAIL_HOST_USER=''
EMAIL_HOST_PASSWORD=''

EMAIL_HOST='smtp.gmailaa.com'
EMAIL_PORT=123
EMAIL_HOST_USER='xyz'
EMAIL_HOST_PASSWORD=''

EMAIL_HOST='smtp.gmaildd.com'
EMAIL_PORT=135
EMAIL_HOST_USER='abc'
EMAIL_HOST_PASSWORD=''

# django-debug-toolbar

#DEBUG_TOOLBAR_PANELS = [

#    'debug_toolbar.panels.timer.TimerPanel',
#    'debug_toolbar.panels.settings.SettingsPanel',
#    'debug_toolbar.panels.headers.HeadersPanel',
#    'debug_toolbar.panels.request.RequestPanel',
#    'debug_toolbar.panels.sql.SQLPanel',
#    'debug_toolbar.panels.templates.TemplatesPanel',
#    'debug_toolbar.panels.staticfiles.StaticFilesPanel',
#    'debug_toolbar.panels.cache.CachePanel',
#    'debug_toolbar.panels.signals.SignalsPanel',
#    'debug_toolbar.panels.logging.LoggingPanel',
#    'debug_toolbar.panels.redirects.RedirectsPanel',
#    'debug_toolbar.panels.profiling.ProfilingPanel',
#]