from django.urls import path
from . import views, categorie_views

urlpatterns = [
    path('produit/', views.produit),
    path('traitement/', views.traitement),
    path("", views.index),
    path("infos/<int:id>/", views.infos),
    path("update/<int:id>/", views.update),
    path("updatetraitement/<int:id>/", views.updatetraitement),
    path("delete/<int:id>/", views.delete),
#pages pour categories
    path('indexcategorie/', categorie_views.index),
    path('ajoutcategorie/', categorie_views.ajout),
    path('traitementcategorie/', categorie_views.traitement),
    path('affichagecategorie/<int:id>/', categorie_views.affiche),
    path('deletecategorie/<int:id>/', categorie_views.delete),
    path('updatecategorie/<int:id>/', categorie_views.update),
    path('traitementupdatecategorie/<int:id>/', categorie_views.updatetraitement),
]
