# plateforme/context_processors.py
from django.conf import settings

def site_info(request):
    """Ajoute des informations du site à tous les templates"""
    return {
        'SITE_NAME': settings.SITE_NAME,
        'SITE_DESCRIPTION': settings.SITE_DESCRIPTION,
        'SITE_AUTHOR': settings.SITE_AUTHOR,
        'DEBUG': settings.DEBUG,
    }
