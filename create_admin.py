import os
import django
import sys

# Configure Django
sys.path.append(os.path.dirname(os.path.abspath(__file__)))
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'plateforme.settings')
django.setup()

from django.contrib.auth.models import User

# TES IDENTIFIANTS
USERNAME = "SVM_CAPC"
EMAIL = "centre_veille_ceeac@capc-ac.net"
PASSWORD = "salle_veille"

print("=== Vérification du superuser ===")

# Vérifie si le superuser existe déjà
if User.objects.filter(username=USERNAME).exists():
    print(f"✅ Superuser '{USERNAME}' existe déjà")
else:
    try:
        # Crée le superuser
        User.objects.create_superuser(
            username=USERNAME,
            email=EMAIL,
            password=PASSWORD
        )
        print(f"✅ Superuser '{USERNAME}' créé avec succès!")
        print(f"   Email: {EMAIL}")
    except Exception as e:
        print(f"❌ Erreur: {e}")
