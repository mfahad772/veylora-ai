import os
from pathlib import Path


# =========================================================
# BASE DIRECTORY
# =========================================================

BASE_DIR = Path(__file__).resolve().parent.parent


# =========================================================
# SECURITY
# =========================================================

SECRET_KEY = os.environ.get(
    "DJANGO_SECRET_KEY",
    "django-insecure-veylora-local-development-only"
)


# Production par default False.
# Local development ke liye environment variable se True kar sakte ho.

DEBUG = (
    os.environ.get(
        "DJANGO_DEBUG",
        "False"
    ).lower()
    == "true"
)


ALLOWED_HOSTS = [
    "127.0.0.1",
    "localhost",
    "192.168.1.4",
    "mfahad2177.pythonanywhere.com",
]


# =========================================================
# INSTALLED APPS
# =========================================================

INSTALLED_APPS = [

    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",

    "allauth",
    "allauth.account",
    "allauth.socialaccount",
    "allauth.socialaccount.providers.google",

    "tools",

]


# =========================================================
# MIDDLEWARE
# =========================================================

MIDDLEWARE = [

    "django.middleware.security.SecurityMiddleware",

    "django.contrib.sessions.middleware.SessionMiddleware",

    "django.middleware.common.CommonMiddleware",

    "django.middleware.csrf.CsrfViewMiddleware",

    "django.contrib.auth.middleware.AuthenticationMiddleware",

    "django.contrib.messages.middleware.MessageMiddleware",

    "allauth.account.middleware.AccountMiddleware",

    "django.middleware.clickjacking.XFrameOptionsMiddleware",

]


# =========================================================
# URL CONFIGURATION
# =========================================================

ROOT_URLCONF = "aiwebsite.urls"


# =========================================================
# TEMPLATES
# =========================================================

TEMPLATES = [

    {

        "BACKEND":
            "django.template.backends.django.DjangoTemplates",

        "DIRS": [],

        "APP_DIRS": True,

        "OPTIONS": {

            "context_processors": [

                "django.template.context_processors.request",

                "django.contrib.auth.context_processors.auth",

                "django.contrib.messages.context_processors.messages",

            ],

        },

    },

]


# =========================================================
# WSGI
# =========================================================

WSGI_APPLICATION = "aiwebsite.wsgi.application"


# =========================================================
# DATABASE
# =========================================================

DATABASES = {

    "default": {

        "ENGINE":
            "django.db.backends.sqlite3",

        "NAME":
            BASE_DIR / "db.sqlite3",

    }

}


# =========================================================
# AUTHENTICATION BACKENDS
# =========================================================

AUTHENTICATION_BACKENDS = [

    "django.contrib.auth.backends.ModelBackend",

    "allauth.account.auth_backends.AuthenticationBackend",

]


# =========================================================
# PASSWORD VALIDATION
# =========================================================

AUTH_PASSWORD_VALIDATORS = [

    {

        "NAME":
            "django.contrib.auth.password_validation.MinimumLengthValidator",

        "OPTIONS": {

            "min_length": 6,

        },

    },

    {

        "NAME":
            "django.contrib.auth.password_validation.CommonPasswordValidator",

    },

    {

        "NAME":
            "django.contrib.auth.password_validation.NumericPasswordValidator",

    },

]


# =========================================================
# LOGIN / LOGOUT
# =========================================================

LOGIN_URL = "/login/"

LOGIN_REDIRECT_URL = "/welcome/"

LOGOUT_REDIRECT_URL = "/"


# =========================================================
# GOOGLE SOCIAL LOGIN
# =========================================================

SOCIALACCOUNT_PROVIDERS = {

    "google": {

        "APP": {

            "client_id":
                os.environ.get(
                    "GOOGLE_CLIENT_ID",
                    ""
                ),

            "secret":
                os.environ.get(
                    "GOOGLE_CLIENT_SECRET",
                    ""
                ),

            "key": "",

        },

        "SCOPE": [

            "profile",
            "email",

        ],

        "AUTH_PARAMS": {

            "access_type":
                "online",

        },

        "OAUTH_PKCE_ENABLED":
            True,

    },

}


SOCIALACCOUNT_QUERY_EMAIL = True

SOCIALACCOUNT_STORE_TOKENS = False

SOCIALACCOUNT_AUTO_SIGNUP = True


# =========================================================
# INTERNATIONALIZATION
# =========================================================

LANGUAGE_CODE = "en-us"

TIME_ZONE = "UTC"

USE_I18N = True

USE_TZ = True


# =========================================================
# STATIC FILES
# =========================================================

STATIC_URL = "static/"


# =========================================================
# EMAIL
# =========================================================

EMAIL_BACKEND = (
    "django.core.mail.backends.console.EmailBackend"
)


# =========================================================
# PRODUCTION COOKIE SECURITY
# =========================================================

SESSION_COOKIE_SECURE = not DEBUG

CSRF_COOKIE_SECURE = not DEBUG


# =========================================================
# SECURITY HEADERS
# =========================================================

X_FRAME_OPTIONS = "DENY"

SECURE_CONTENT_TYPE_NOSNIFF = True

SECURE_REFERRER_POLICY = "same-origin"


# =========================================================
# DEFAULT PRIMARY KEY
# =========================================================

DEFAULT_AUTO_FIELD = (
    "django.db.models.BigAutoField"
)