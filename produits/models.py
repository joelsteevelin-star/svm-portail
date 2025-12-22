from django.db import models
from django.contrib.auth.models import User

class Categorie(models.Model):
    nom = models.CharField(max_length=100)
    slug = models.SlugField(unique=True, blank=True)
    description = models.TextField(blank=True)
    
    def __str__(self):
        return self.nom

class Produit(models.Model):
    TYPE_CHOICES = [
        ('pdf', 'Bulletin (PDF)'),
        ('image', 'Carte (Image)'),
        ('service', 'Service'),
        ('physique', 'Produit Physique'),
    ]
    
    nom = models.CharField(max_length=200)
    slug = models.SlugField(unique=True, blank=True)
    description = models.TextField()
    description_courte = models.CharField(max_length=300, blank=True)
    prix = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    categorie = models.ForeignKey(Categorie, on_delete=models.SET_NULL, null=True, blank=True)
    type_produit = models.CharField(max_length=20, choices=TYPE_CHOICES, default='pdf')
    
    # Pour les fichiers (PDF/Images)
    fichier = models.FileField(upload_to='produits/fichiers/', blank=True, null=True)
    
    # Pour les images produits
    image_principale = models.ImageField(upload_to='produits/images/', blank=True)
    
    # Métadonnées
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='produits_crees')
    created_at = models.DateTimeField(auto_now_add=True)
    is_published = models.BooleanField(default=True)
    stock = models.PositiveIntegerField(default=0)
    
    def __str__(self):
        return self.nom
    
    def save(self, *args, **kwargs):
        if not self.slug:
            from django.utils.text import slugify
            self.slug = slugify(self.nom)
        super().save(*args, **kwargs)
