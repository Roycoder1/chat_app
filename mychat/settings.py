"""
Django settings for mychat project.

Generated by 'django-admin startproject' using Django 4.0.4.

For more information on this file, see
https://docs.djangoproject.com/en/4.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.0/ref/settings/
"""

from pathlib import Path
import os
# import environ
import django_heroku
# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-lcv2ee6#vr@@kquoa4_z!v5me=t1vre(@f@zhohbyj=b&8$d18'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True
# env = environ.Env(
#     # set casting, default value
#     DEBUG=(bool, False)
# )

# environ.Env.read_env(os.path.join(BASE_DIR, '.env'))


# DEBUG=env('DEBUG')

ALLOWED_HOSTS = ['chatroyapp.herokuapp.com']
# ALLOWED_HOSTS = ['*']




# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    # 'whitenoise.runserver_nostatic',
    'django.contrib.staticfiles',
    'mychatapp'
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    # 'whitenoise.middleware.WhiteNoiseMiddleware',
]

ROOT_URLCONF = 'mychat.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
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

WSGI_APPLICATION = 'mychat.wsgi.application'


# Database
# https://docs.djangoproject.com/en/4.0/ref/settings/#databases



DATABASES = {
    "default": {
        'ENGINE': 'django.db.backends.postgresql',
        "NAME": "abra_chat",
        'USER': 'postgres',
        'PASSWORD': 'Azerty1234567890',
        'HOST': 'localhost',
        'PORT': '5432',
        
    }
}
# DATABASES = {
#     "default": {
#         'ENGINE': 'django.db.backends.postgresql',
#         "NAME": "d855th4bgfg2c6",
#         'USER': 'hnclrxuglmngsq',
#         'PASSWORD': '88e23ed7239d481e36ee11f4f6e9fc8330a9d06f662629b387c65784d38dee99',
#         'HOST': 'ec2-35-173-91-114.compute-1.amazonaws.com',
#         'PORT': '5432',
#     }
# }


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


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.0/howto/static-files/
# STATIC_ROOT=os.path.join()
# STATIC_URL = 'static/'
STATICFILES_DIRS = [BASE_DIR/'static']
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
# STATIC_ROOT='static_root'
STATIC_URL = "/static/"
django_heroku.settings(locals())

MEDIA_URL = 'media/'

MEDIA_ROOT = BASE_DIR/'static'

# Default primary key field type
# https://docs.djangoproject.com/en/4.0/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
LOGIN_REDIRECT_URL = 'home' 
