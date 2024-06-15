from os import path
from requests import get
from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-=cldztbc4jg&xl0!x673!*v2_=p$$eu)=7*f#d0#zs$44xx-h^'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

ALLOWED_HOSTS = ['*']

# DISCORD: Bot Token
BOT_TOKEN = 'MTIyMDA5MTQ3NDY3MTMwODkyMA.GOOFNZ.VMeR718L6FKYLlUOIqwrQ6YVY86Sgp0dK5KdZQ'

# DISCORD: http header
DISCORD_AUTH = {
  'Authorization': f'Bot {BOT_TOKEN}'
}

# DISCORD: Global Endpoints
DISCORD_API_BASE = 'https://discord.com/api/v10'
DISCORD_IMAGE_BASE = 'https://cdn.discordapp.com'

# DISCORD: Global IDs
GUILD_ID = '1217879394941534330'

# Guild data: Fetch, Data
GUILD_FETCHING = get(url=f'{DISCORD_API_BASE}/guilds/{GUILD_ID}', params={'with_counts': True}, headers=DISCORD_AUTH)
GUILD_DATA = GUILD_FETCHING.json() if GUILD_FETCHING.status_code == 200 else None

OWNER_FETCHING = get(url=f'{DISCORD_API_BASE}/users/{GUILD_DATA["owner_id"]}', headers=DISCORD_AUTH)
OWNER_DATA = OWNER_FETCHING.json() if OWNER_FETCHING.status_code == 200 else None

# GUILD:
GUILD_MEMBERS_COUNT = GUILD_DATA['approximate_member_count']
OWNER_USERNAME = OWNER_DATA['username']
OWNER_GLOBAL_NAME = OWNER_DATA['global_name']

# SITE:
SITE_NAME = GUILD_DATA['name']
FAVICON = f"{DISCORD_IMAGE_BASE}/icons/{GUILD_ID}/{GUILD_DATA['icon']}.png"

# META:
META_SITE_NAME = "Gameplay Avançada"
DESCRIPTION = f'''
{SITE_NAME} está atualmente na posse de @{OWNER_USERNAME} (também conhecido como {OWNER_GLOBAL_NAME}).
Os mitinhos estão mais ativos do que nunca!!!!!
'''

# Application definition
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    
    # Internals
    'discord',
    'pages',
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

ROOT_URLCONF = 'api.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [path.join(BASE_DIR, 'templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',

                # externals
                'django_settings_export.settings_export'
            ],
        },
    },
]

WSGI_APPLICATION = 'api.wsgi.app'


# Database
# https://docs.djangoproject.com/en/4.1/ref/settings/#databases
# Note: Django modules for using databases are not support in serverless
# environments like Vercel. You can use a database over HTTP, hosted elsewhere.

DATABASES = {}


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

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.1/howto/static-files/

STATIC_URL = '/static/'
STATICFILES_DIRS = path.join(BASE_DIR, 'static'),
STATIC_ROOT = path.join(BASE_DIR, 'staticfiles_build', 'static')
STATICFILES_DIRS = [
    BASE_DIR / 'static',
]
# Default primary key field type
# https://docs.djangoproject.com/en/4.1/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# Context processors: django-settings-export
SETTINGS_EXPORT = [
    'SITE_NAME',
    'FAVICON',
    'DESCRIPTION',
    'META_SITE_NAME'
]
