# Create your models here.
from django.db import models

class Produit(models.Model):
    TYPE_CHOICES = [
        ('pdf', 'Bulletin (PDF)'),
        ('image', 'Carte (Image)'),
    ]

    titre = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    type = models.CharField(max_length=10, choices=TYPE_CHOICES)
    fichier = models.FileField(upload_to='uploads/')
    stock = models.PositiveIntegerField(default=0)
    date_ajout = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.titre
