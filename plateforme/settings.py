"""
Django settings for plateforme project.
Configuration optimisée pour la production avec hébergement Render/Railway
"""

import os
from pathlib import Path
import dj_database_url
from decouple import config
import sys

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# ==================== SÉCURITÉ ====================
# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = config('SECRET_KEY', default='django-insecure-clé-temporaire-pour-développement')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = config('DEBUG', default=False, cast=bool)

# Hosts autorisés
ALLOWED_HOSTS = [
    'localhost',
    '127.0.0.1',
    '.onrender.com',  # Pour Render
    '.railway.app',   # Pour Railway
    '.svm-portail.com',  # Ton domaine personnalisé
]

# Protection CSRF
CSRF_TRUSTED_ORIGINS = [
    'https://*.onrender.com',
    'https://*.railway.app',
    'https://*.svm-portail.com',
]

# ==================== APPLICATIONS ====================
INSTALLED_APPS = [
    # Django core
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    
    # Apps tierces
    "crispy_forms",
    "crispy_bootstrap5",
    
    # Tes applications
    "produits",
#     "comptes",  # À créer pour la gestion utilisateur
#     "pages",    # À créer pour pages statiques
]

# Configuration Crispy Forms
CRISPY_ALLOWED_TEMPLATE_PACKS = "bootstrap5"
CRISPY_TEMPLATE_PACK = "bootstrap5"

# ==================== MIDDLEWARE ====================
MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "whitenoise.middleware.WhiteNoiseMiddleware",  # Pour fichiers statiques en production
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

# ==================== TEMPLATES ====================
TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [
            BASE_DIR / "templates",  # Dossier global pour templates
        ],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
                # Context processor personnalisé pour ton site
                "plateforme.context_processors.site_info",
            ],
        },
    },
]

# ==================== BASE DE DONNÉES ====================
# Configuration adaptative (SQLite en dev, PostgreSQL en production)
if 'test' in sys.argv or DEBUG:
    # Mode développement/test
    DATABASES = {
        "default": {
            "ENGINE": "django.db.backends.sqlite3",
            "NAME": BASE_DIR / "db.sqlite3",
        }
    }
else:
    # Mode production - utilise PostgreSQL
    DATABASES = {
        "default": dj_database_url.config(
            default=config('DATABASE_URL'),
            conn_max_age=600,
            conn_health_checks=True,
            ssl_require=True
        )
    }

# ==================== FICHIERS STATIQUES & MÉDIAS ====================
# URL pour fichiers statiques
STATIC_URL = "static/"

# Dossier où collecter les fichiers statiques pour la production
STATIC_ROOT = BASE_DIR / "staticfiles"

# Dossiers supplémentaires pour les fichiers statiques
STATICFILES_DIRS = [
    BASE_DIR / "static",  # Ton dossier static personnalisé
]

# Configuration WhiteNoise (optimisation statiques)
STATICFILES_STORAGE = "whitenoise.storage.CompressedManifestStaticFilesStorage"

# Fichiers média (uploads utilisateurs)
MEDIA_URL = "media/"
MEDIA_ROOT = BASE_DIR / "media"

# ==================== INTERNATIONALISATION ====================
LANGUAGE_CODE = "fr-fr"  # Changé pour français
TIME_ZONE = "Europe/Paris"  # Changé pour Paris
USE_I18N = True
USE_TZ = True

# ==================== PERSONNALISATIONS SITE ====================
# Nom de ta plateforme
SITE_NAME = "SVM_PORTAIL"
SITE_DESCRIPTION = "Portail professionnel de gestion des produits Multirisques"
SITE_AUTHOR = "Équipe SVM"

# Configuration email (pour inscriptions)
EMAIL_BACKEND = config('EMAIL_BACKEND', 
    default='django.core.mail.backends.console.EmailBackend')
EMAIL_HOST = config('EMAIL_HOST', default='')
EMAIL_PORT = config('EMAIL_PORT', default=587, cast=int)
EMAIL_USE_TLS = config('EMAIL_USE_TLS', default=True, cast=bool)
EMAIL_HOST_USER = config('EMAIL_HOST_USER', default='')
EMAIL_HOST_PASSWORD = config('EMAIL_HOST_PASSWORD', default='')
DEFAULT_FROM_EMAIL = config('DEFAULT_FROM_EMAIL', 
    default='contact@svm-portail.com')

# ==================== URL CONFIGURATION ====================
ROOT_URLCONF = "plateforme.urls"
WSGI_APPLICATION = "plateforme.wsgi.application"

# ==================== SECURITY SETTINGS ====================
# HTTPS settings
SECURE_SSL_REDIRECT = not DEBUG  # Redirection HTTPS en production
SESSION_COOKIE_SECURE = not DEBUG
CSRF_COOKIE_SECURE = not DEBUG
SECURE_BROWSER_XSS_FILTER = True
SECURE_CONTENT_TYPE_NOSNIFF = True

# ==================== LOGGING ====================
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'verbose': {
            'format': '{levelname} {asctime} {module} {message}',
            'style': '{',
        },
    },
    'handlers': {
        'console': {
            'class': 'logging.StreamHandler',
            'formatter': 'verbose',
        },
    },
    'loggers': {
        'django': {
            'handlers': ['console'],
            'level': 'INFO',
        },
        'plateforme': {
            'handlers': ['console'],
            'level': 'DEBUG' if DEBUG else 'INFO',
        },
    },
}
