from .base import *

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['twiter-api.herokuapp.com']

# Database
# https://docs.djangoproject.com/en/3.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'd1h45g6homgj82',
        'USER': 'lcuvutzjmeungl' ,
        'PASSWORD':'90ecc06f9ae428c73e4cd575811bb30472aa8a0987adde84ebe99f62abcedd26',
        'HOST':'ec2-54-159-35-35.compute-1.amazonaws.com',
        'PORT': 5432,
    }
}


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.0/howto/static-files/

STATIC_URL = '/static/'

STATICFILES_DIRS = (BASE_DIR,'static')

CORS_ALLOWED_ORIGINS = [
    "http://localhost:3000",
    "http://localhost:3000/checkout",
    "http://localhost:3000/api",
    "https://miguesc2.github.io/",
]

CORS_ORIGIN_WHITELIST = [
    "http://localhost:3000",
    "http://localhost:3000/checkout",
    "http://localhost:3000/api",
    "https://miguesc2.github.io/",
]
