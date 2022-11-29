"""
Django settings for do_it_django_prj project.

Generated by 'django-admin startproject' using Django 4.1.2.

For more information on this file, see
https://docs.djangoproject.com/en/4.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.1/ref/settings/
"""

from pathlib import Path
import os
import my_settings

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure--qnpxp**5w-utf+tica$so^io7)rqcuj$59*d+1t(-6q1lgwhy'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['127.0.0.1', 'localhost', 'bd49-121-159-54-81.jp.ngrok.io']


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django_bootstrap5',
    'accounts',
    'blog',
    'diary',
    'single_pages',
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

ROOT_URLCONF = 'do_it_django_prj.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            BASE_DIR / "do_it_django_prj" / "templates",
        ],
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

WSGI_APPLICATION = 'do_it_django_prj.wsgi.application'


# Database
# https://docs.djangoproject.com/en/4.1/ref/settings/#databases

# DATABASES = my_settings.DATABASES
DATABASES = {
    "default": {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'Project_test2', #2
        'USER': 'admin', #3
        'PASSWORD': 'admin',  #4
        'HOST': 'localhost',   #5                
        'PORT': '3306', #6
    }
}



# Password validation
# https://docs.djangoproject.com/en/4.1/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/4.1/topics/i18n/

LANGUAGE_CODE = 'ko-kr'

TIME_ZONE = 'Asia/Seoul'

USE_I18N = True

USE_TZ = False


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.1/howto/static-files/

STATIC_URL = 'static/'

# 장고앱/static 은 자동으로 장고가 찾아내요.
# 다른 경로에 있는 static 폴더는 STATICFILES_DIRS에 추가해줘야, 장고가 찾습니다.
STATICFILES_DIRS = [
    BASE_DIR / "do_it_django_prj" / "static",  # 지금의 BASE_DIR은 Path 객체
    # os.path.join(BASE_DIR, 'do_it_django_prj','static'),  # BASE_DIR은 문자열이었어요.
]

# STATIC_DIRS =[
#     os.path.join(BASE_DIR, 'do_it_django_prj', 'static') 
# ]

#static 파일을 모을 디렉터리
# 각 장고앱내의 static 파일들을 STATIC_ROOT에 지정한 경로로 복사 => collectstatic 명령
# STATIC_ROOT = BASE_DIR / 'static'   # os.path.join(BASE_DIR, 'static')

# Default primary key field 1type
# https://docs.djangoproject.com/en/4.1/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

INTERNAL_IPS = ['127.0.0.1']

# MEDIA_URL = '/media/'
# MEDIA_ROOT = BASE_DIR / '_media'  # os.path.join(BASE_DIR, '_media')


MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media'  # os.path.join(BASE_DIR, 'media')
