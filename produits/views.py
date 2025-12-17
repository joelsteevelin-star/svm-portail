from django.shortcuts import render
from django.http import HttpResponse

def liste_produits(request):
    return render(request, 'produits/liste.html')

def detail_produit(request, slug):
    return render(request, 'produits/detail.html')
