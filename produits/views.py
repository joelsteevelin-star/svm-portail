from django.shortcuts import render, get_object_or_404
from .models import Produit, Categorie

def liste_produits(request):
    """
    Affiche tous les produits publiés, avec filtrage par catégorie optionnel
    """
    # Récupère tous les produits PUBLIÉS (is_published=True)
    produits = Produit.objects.filter(is_published=True).order_by('-created_at')
    
    # Filtre par catégorie si un slug de catégorie est fourni dans l'URL
    categorie_slug = request.GET.get('categorie')
    if categorie_slug:
        categorie = get_object_or_404(Categorie, slug=categorie_slug)
        produits = produits.filter(categorie=categorie)
    
    # Récupère toutes les catégories pour le menu de filtrage
    categories = Categorie.objects.all()
    
    context = {
        'produits': produits,
        'categories': categories,
        'categorie_active': categorie_slug,
    }
    return render(request, 'produits/liste.html', context)

def detail_produit(request, slug):
    """
    Affiche le détail d'un produit spécifique
    """
    produit = get_object_or_404(Produit, slug=slug, is_published=True)
    
    # Produits similaires (même catégorie)
    produits_similaires = Produit.objects.filter(
        categorie=produit.categorie,
        is_published=True
    ).exclude(id=produit.id)[:4]
    
    context = {
        'produit': produit,
        'produits_similaires': produits_similaires,
    }
    return render(request, 'produits/detail.html', context)
