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

DEBUG = True


ALLOWED_HOSTS = [
    "127.0.0.1",
    "localhost",
    "192.168.1.4",
    "mfahad2177.pythonanywhere.com",
]


# =========================================================
# APPLICATIONS
# =========================================================

INSTALLED_APPS = [

    # Django
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",

    # django-allauth
    "allauth",
    "allauth.account",
    "allauth.socialaccount",

    # Google OAuth
    "allauth.socialaccount.providers.google",

    # Veylora AI
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

    # Required by django-allauth
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
        "BACKEND": "django.template.backends.django.DjangoTemplates",

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

        "ENGINE": "django.db.backends.sqlite3",

        "NAME": BASE_DIR / "db.sqlite3",

    }

}


# =========================================================
# AUTHENTICATION BACKENDS
# =========================================================

AUTHENTICATION_BACKENDS = [

    # Normal Django username/password
    "django.contrib.auth.backends.ModelBackend",

    # django-allauth / Google
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
# LOGIN / LOGOUT / WELCOME REDIRECTS
# =========================================================

# Our custom Veylora AI login page
LOGIN_URL = "/login/"


# Normal Django + Google login success
LOGIN_REDIRECT_URL = "/welcome/"


# Logout goes back to homepage
LOGOUT_REDIRECT_URL = "/"


# =========================================================
# GOOGLE SOCIAL LOGIN
# =========================================================

SOCIALACCOUNT_PROVIDERS = {

    "google": {

        # Google Cloud credentials
        "APP": {

            "client_id": os.environ.get(
                "GOOGLE_CLIENT_ID",
                ""
            ),

            "secret": os.environ.get(
                "GOOGLE_CLIENT_SECRET",
                ""
            ),

            "key": "",
        },


        # Google permissions
        "SCOPE": [
            "profile",
            "email",
        ],


        "AUTH_PARAMS": {
            "access_type": "online",
        },


        # Extra OAuth security
        "OAUTH_PKCE_ENABLED": True,
    },
}


# Allow allauth to obtain email from Google
SOCIALACCOUNT_QUERY_EMAIL = True


# We do not need to permanently save Google's access token
SOCIALACCOUNT_STORE_TOKENS = False


# Automatically create Veylora account
# when Google authentication succeeds
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
# DEFAULT PRIMARY KEY
# =========================================================

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"