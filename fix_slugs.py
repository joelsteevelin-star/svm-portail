#!/usr/bin/env python
import os
import sys
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'plateforme.settings')
django.setup()

from produits.models import Produit
from django.utils.text import slugify

print("=== Correction des slugs avant migration ===")

# Pour chaque produit sans slug ou avec slug vide
for produit in Produit.objects.filter(slug__isnull=True) | Produit.objects.filter(slug=''):
    old_slug = produit.slug
    new_slug = slugify(produit.nom)
    
    # Assure l'unicité
    counter = 1
    base_slug = new_slug
    while Produit.objects.filter(slug=new_slug).exists():
        new_slug = f"{base_slug}-{counter}"
        counter += 1
    
    produit.slug = new_slug
    produit.save()
    print(f"✅ {produit.nom}: '{old_slug}' → '{new_slug}'")

print(f"=== {Produit.objects.count()} produits vérifiés ===")
