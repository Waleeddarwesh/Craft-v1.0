# ==============================================================================
# CORE DJANGO IMPORTS & ENVIRONMENT SETUP
# ==============================================================================
import os
import dj_database_url
from datetime import timedelta
from pathlib import Path
from environ import Env
from celery.schedules import crontab

# Initialize the environment variable reader
env = Env()

# --- Environment Configuration ---
# Set the default environment to 'production' if not specified
ENVIRONMENT = env('ENVIRONMENT', default='production')
# Define the base directory of the project
BASE_DIR = Path(__file__).resolve().parent.parent
# Read the .env file for environment-specific variables
env.read_env(env_file=BASE_DIR / '.env')


# ==============================================================================
# SECURITY & DEPLOYMENT SETTINGS
# ==============================================================================

# --- Secret Key ---
# A secret key used for cryptographic signing. Keep this secret!
SECRET_KEY = env('SECRET_KEY')

# --- Debug Mode ---
# Set to True for development to get detailed error pages.
# Should ALWAYS be False in production for security.
DEBUG = env.bool('DEBUG', default=False)


# --- Host Configuration ---
# A list of strings representing the host/domain names that this Django site can serve.
ALLOWED_HOSTS = ['localhost', 'craft.up.railway.app','crafteg.up.railway.app', '127.0.0.1']
# A list of trusted origins for unsafe requests (e.g., POST).
CSRF_TRUSTED_ORIGINS = ["https://craft.up.railway.app", "http://craft.up.railway.app",
                        "https://crafteg.up.railway.app","http://crafteg.up.railway.app"]


# ==============================================================================
# INSTALLED APPLICATIONS
# ==============================================================================
# Core Django applications, third-party packages, and your project's apps are listed here.
INSTALLED_APPS = [
    # Admin interface enhancements
    'admin_interface',
    'colorfield',

    # ASGI & Channels for WebSockets
    'daphne',
    'channels',

    # CORS headers for cross-origin requests
    'corsheaders',

    # Django core apps
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    # Static file handling for production
    'whitenoise.runserver_nostatic',

    # Third-party apps
    'social_django',
    'rest_framework_swagger',
    'drf_yasg',
    'rest_framework',
    'django_filters',
    'rest_framework_simplejwt.token_blacklist',
    'django_celery_beat',

    # project's applications
    'accounts',
    'products',
    'course',
    'orders',
    'reviews',
    'payment',
    'notifications',
    'chatapp',
    'returnrequest',
    'recommendations',
]


# ==============================================================================
# MIDDLEWARE CONFIGURATION
# ==============================================================================
# A list of middleware to be executed for each request/response cycle.
# Order is important.
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware', # For serving static files
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.middleware.locale.LocaleMiddleware',
    'corsheaders.middleware.CorsMiddleware',
]


# ==============================================================================
# AUTHENTICATION & SOCIAL AUTH
# ==============================================================================

# --- Authentication Backends ---
# Specifies how users are authenticated.
AUTHENTICATION_BACKENDS = [
    'social_core.backends.google.GoogleOAuth2',
    'social_core.backends.facebook.FacebookOAuth2',
    'django.contrib.auth.backends.ModelBackend',
]

# --- Custom User Model ---
AUTH_USER_MODEL = 'accounts.User'

# --- Social Auth Settings ---
SOCIAL_AUTH_LOGIN_REDIRECT_URL = '/accounts/social-complete/'
SOCIAL_AUTH_NEW_USER_REDIRECT_URL = '/accounts/social-complete/'
SOCIAL_AUTH_GOOGLE_OAUTH2_KEY = env('GOOGLE_CLIENT_ID')
SOCIAL_AUTH_GOOGLE_OAUTH2_SECRET = env('GOOGLE_CLIENT_SECRET')
SOCIAL_AUTH_GOOGLE_OAUTH2_SCOPE = [
    'https://www.googleapis.com/auth/userinfo.email',
    'https://www.googleapis.com/auth/userinfo.profile',
]
SOCIAL_AUTH_PASSWORD = env('SOCIAL_AUTH_PASSWORD', default='craft-social-login')
SOCIAL_AUTH_FACEBOOK_KEY = env('SOCIAL_AUTH_FACEBOOK_KEY')
SOCIAL_AUTH_FACEBOOK_SECRET = env('SOCIAL_AUTH_FACEBOOK_SECRET')
SOCIAL_AUTH_FACEBOOK_SCOPE = ['email', 'public_profile']
SOCIAL_AUTH_FACEBOOK_PROFILE_EXTRA_PARAMS = {
    'fields': 'id, name, email, first_name, last_name'
}
SOCIAL_AUTH_PIPELINE = (
    'social_core.pipeline.social_auth.social_details',
    'social_core.pipeline.social_auth.social_uid',
    'social_core.pipeline.social_auth.auth_allowed',
    'social_core.pipeline.social_auth.social_user',
    'social_core.pipeline.user.get_username',
    'accounts.pipeline.create_temp_user',
)


# ==============================================================================
# REST FRAMEWORK & JWT
# ==============================================================================

# --- Django Rest Framework ---
REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework_simplejwt.authentication.JWTAuthentication',
    ),
    'DEFAULT_RENDERER_CLASSES': [
        'rest_framework.renderers.JSONRenderer',
    ]
}

# --- Simple JWT Settings ---
SIMPLE_JWT = {
    'ACCESS_TOKEN_LIFETIME': timedelta(days=1),
    'REFRESH_TOKEN_LIFETIME': timedelta(days=1),
    'ROTATE_REFRESH_TOKENS': True,
    'BLACKLIST_AFTER_ROTATION': True,
    'AUTH_HEADER_TYPES': ('Bearer',),
    'AUTH_TOKEN_CLASSES': ('rest_framework_simplejwt.tokens.AccessToken',),
}


# ==============================================================================
# URL & APPLICATION CONFIGURATION
# ==============================================================================

# The root URL configuration for the project.
ROOT_URLCONF = 'Handcrafts.urls'

# The entry points for WSGI and ASGI servers.
WSGI_APPLICATION = 'Handcrafts.wsgi.application'
ASGI_APPLICATION = 'Handcrafts.asgi.application'


# ==============================================================================
# TEMPLATES
# ==============================================================================
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
                'social_django.context_processors.backends',
                'social_django.context_processors.login_redirect',
            ],
        },
    },
]


# ==============================================================================
# DATABASE CONFIGURATION
# ==============================================================================
DATABASES = {
    "default": dj_database_url.parse(env('DATABASE_URL'))
}


# ==============================================================================
# REDIS, CHANNELS & CELERY
# ==============================================================================

REDIS_URL = env('REDIS_URL', default='redis://localhost:6379/0')

# --- Celery configuration ---
CELERY_BROKER_URL = REDIS_URL
CELERY_RESULT_BACKEND = REDIS_URL
CELERY_ACCEPT_CONTENT = ['json']
CELERY_TASK_SERIALIZER = 'json'
CELERY_RESULT_SERIALIZER = 'json'
CELERY_TIMEZONE = 'Africa/Cairo'

# --- Channels configuration ---
CHANNEL_LAYERS = {
    "default": {
        "BACKEND": "channels_redis.core.RedisChannelLayer",
        "CONFIG": {
            "hosts": [REDIS_URL],
        },
    },
}

# --- Caching configuration ---
CACHES = {
    "default": {
        "BACKEND": "django_redis.cache.RedisCache",
        "LOCATION": REDIS_URL,
        "OPTIONS": {
            "CLIENT_CLASS": "django_redis.client.DefaultClient",
        }
    }
}
# --- Session configuration ---
SESSION_ENGINE = "django.contrib.sessions.backends.cache"
SESSION_CACHE_ALIAS = "default"

# --- Celery Beat Scheduler ---
# Defines periodic tasks for Celery.

# CELERY_BEAT_SCHEDULER = 'django_celery_beat.schedulers:DatabaseScheduler'
# CELERY_BEAT_SCHEDULE = {
#     'update-recommendations-daily': {
#         'task': 'recommendations.tasks.update_recommendations_task',
#         'schedule': crontab(hour=1, minute=30), # Runs every day at 1:30 AM
#     },
#     'cancel-pending-orders': {
#         'task': 'orders.tasks.cancel_pending_credit_card_orders_task',
#         'schedule': crontab(hour=0, minute=0),  # Run every day at midnight
#     },
# }

# Keep these set to True if you want to Pause Celery tasks. 
# This forces user tasks (like emails) to run immediately without a worker process.
CELERY_TASK_ALWAYS_EAGER = True
CELERY_TASK_EAGER_PROPAGATES = True


# ==============================================================================
# STATIC & MEDIA FILES
# ==============================================================================

# --- Static Files ---
# URL to use when referring to static files.
STATIC_URL = '/static/'
# The absolute path to the directory where collectstatic will collect static files.
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
# Storage backend for static files, optimized for production.
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

# --- Media Files ---
# The directory where user-uploaded files will be stored.
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
# The URL that handles the media served from MEDIA_ROOT.
MEDIA_URL = '/media/'


# ==============================================================================
# EXTERNAL SERVICES
# ==============================================================================

# --- Stripe ---
STRIPE_SECRET_KEY = env('STRIPE_SECRET_KEY')
STRIPE_PUBLISHABLE_KEY = env('STRIPE_PUBLISHABLE_KEY')
STRIPE_WEBHOOK_SECRET = env('STRIPE_WEBHOOK_SECRET')

# --- Email ---
EMAIL_BACKEND = 'sendgrid_backend.SendgridBackend'
SENDGRID_API_KEY = env('SENDGRID_API_KEY')
EMAIL_HOST = 'smtp.sendgrid.net'
EMAIL_HOST_USER = 'apikey'  
EMAIL_HOST_PASSWORD = SENDGRID_API_KEY
DEFAULT_FROM_EMAIL = env('DEFAULT_FROM_EMAIL')
EMAIL_PORT = 587
EMAIL_USE_TLS = True

# ==============================================================================
# INTERNATIONALIZATION & MISCELLANEOUS
# ==============================================================================

# --- INTERNATIONALIZATION ---
LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'Africa/Cairo'
USE_I_18_N = True
USE_TZ = True

# --- CORS ---
# A list of origins that are authorized to make cross-site HTTP requests.
CORS_ALLOWED_ORIGINS = [
    "https://craft.up.railway.app",
    "https://crafteg.up.railway.app",
    "http://localhost:8000",
    "http://127.0.0.1:8000",
]

# --- Production Security ---
# These settings are enabled when not in a development environment.
if ENVIRONMENT != 'development':
    SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')
    SECURE_SSL_REDIRECT = True
    SESSION_COOKIE_SECURE = True
    CSRF_COOKIE_SECURE = True

# --- Password Validation ---
AUTH_PASSWORD_VALIDATORS = [
    {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator'},
    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator'},
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator'},
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator'},
]

# --- Default Primary Key ---
# The default primary key field type to use for models.
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
