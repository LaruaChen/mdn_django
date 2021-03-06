"""
Django settings for locallibrary project.

Generated by 'django-admin startproject' using Django 3.1.2.

For more information on this file, see
https://docs.djangoproject.com/en/3.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.1/ref/settings/
"""

import os
from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
# SECRET_KEY = 'c8kjvw19ftijbtee+97pm8gta!-k2&3&l=2cq_ply)461sdy4a'

# Read SECRET_KEY from an environment variable
import os
import psycopg2
SECRET_KEY = os.environ.get('DJANGO_SECRET_KEY', 'c8kjvw19ftijbtee+97pm8gta!-k2&3&l=2cq_ply)461sdy4a')

# SECURITY WARNING: don't run with debug turned on in production! 上線時記得改成false
# DEBUG = True
DEBUG = bool( os.environ.get('DJANGO_DEBUG', True) )

ALLOWED_HOSTS = ['dry-lowlands-78164.herokuapp.com', '127.0.0.1']


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth', #Core authentication framework and its default models.
    'django.contrib.contenttypes', #Django content type system (allows permissions to be associated with models).
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'catalog.apps.CatalogConfig', 
]

# 'catalog.apps.CatalogConfig', 註冊新功能且django會同時新增在app.py中

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',  #Manages sessions across requests
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware', #Associates users with requests using sessions. 登入登出
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'locallibrary.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': ['./templates',], #可更快找到html檔
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

WSGI_APPLICATION = 'locallibrary.wsgi.application'


# Database
# https://docs.djangoproject.com/en/3.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'df3tukhgo2t2jq',
        'USER': 'ljdhikpkwnenoo',
        'PASSWORD': '411ced30a9bddd482c72a8652cf6af1d2e89458ff565c9311ed778eb6ddf91c2',
        'HOST': 'ec2-54-164-134-207.compute-1.amazonaws.com',
        'PORT': '5432',
    }
}


# Password validation
# https://docs.djangoproject.com/en/3.1/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/3.1/topics/i18n/

LANGUAGE_CODE = 'zh-hant'

TIME_ZONE = 'Asia/Taipei'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.0/howto/static-files/

# The absolute path to the directory where collectstatic will collect static files for deployment.
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')

# The URL to use when referring to static files (where they will be served from)
STATIC_URL = '/static/'

# Redirect to catalog URL after login 登入後設定導入首頁 (Default redirects to /accounts/profile/)
LOGIN_REDIRECT_URL = '/'
# LOGOUT_REDIRECT_URL = '/'

# 密碼重設系統要求您的網站支持電子郵件，這將記錄發送到控制台的所有電子郵件（因此您可以從控制台複製密碼重置鏈接）
EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

# Simplified static file serving.提供靜態文件時減小它們的大小（效率更高）
# https://warehouse.python.org/project/whitenoise/
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

# Heroku: Update database configuration from $DATABASE_URL.
import dj_database_url
db_from_env = dj_database_url.config(conn_max_age=500)
DATABASES['default'].update(db_from_env)