from django.urls import path
from . import views

app_name = 'produits'

urlpatterns = [
    path('', views.liste_produits, name='produit_liste'),
    path('<slug:slug>/', views.detail_produit, name='produit_detail'),
]
