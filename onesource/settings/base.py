"""
Django settings for onesource project.

For more information on this file, see
https://docs.djangoproject.com/en/1.6/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.6/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.6/howto/deployment/checklist/


ALLOWED_HOSTS = ['*', ]


# Application definition

INSTALLED_APPS = (
    'grappelli.dashboard',
    'grappelli',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.formtools',
    'ordered_model',
    'autoslug',
    'ckeditor',
    'compressor',
    'imagekit',
    'multiselectfield',
    'sections',
    'journal',
    'layout_elements',
    'pages',
    'contact',
    'news',
    'jobs',
    'gwac',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

TEMPLATE_CONTEXT_PROCESSORS = (
    "django.contrib.auth.context_processors.auth",
    "django.core.context_processors.request",
    "django.core.context_processors.i18n",
    'django.contrib.messages.context_processors.messages',
)

ROOT_URLCONF = 'onesource.urls'

WSGI_APPLICATION = 'onesource.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.6/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'onesource',
        'USER': 'root',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}


# Internationalization
# https://docs.djangoproject.com/en/1.6/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'America/New_York'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.6/howto/static-files/

STATIC_URL = '/static/'

STATICFILES_DIRS = (
    os.path.join(BASE_DIR, '../static'),
)

STATIC_ROOT = os.path.join(BASE_DIR, '../static_final')

STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
    'compressor.finders.CompressorFinder',
)

TEMPLATE_DIRS = (
    os.path.join(BASE_DIR, '../templates'),
)

MEDIA_ROOT = os.path.join(BASE_DIR, '../media')

MEDIA_URL = '/media/'

CKEDITOR_UPLOAD_PATH = 'uploads/'

CKEDITOR_JQUERY_URL = '//ajax.googleapis.com/ajax/libs/jquery/2.1.3/jquery.min.js'

GRAPPELLI_ADMIN_TITLE = '1Source Admin'

GRAPPELLI_CLEAN_INPUT_TYPES = False

GRAPPELLI_INDEX_DASHBOARD = 'onesource.dashboard.CustomIndexDashboard'

CKEDITOR_CONFIGS = {
    'default': {
        'toolbar': [
            ['-', 'Bold', 'Italic', 'Underline',
             '-', 'Link', 'Unlink', 'Styles',
             ],
            ['-', 'Image',
             '-', 'BulletedList', 'NumberedList',
             '-', 'Copy', 'PasteText', 'PasteFromWord',
             '-', 'Source',
             ]
        ],
        'width': 840,
        'height': 200,
        'toolbarCanCollapse': False,
    }
}

EMAIL_HOST_PORT = 587
EMAIL_USE_TLS = True
EMAIL_HOST_USER = 'noreply@1-sc.com'

# uncomment and fill in local_settings
# EMAIL_HOST = ''
# EMAIL_HOST_PASSWORD = ''

GWAC_EMAILS = ['devon.warren@1-sc.com']
