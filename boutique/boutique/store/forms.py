from django.forms import ModelForm
from django.utils.translation import gettext_lazy as _
from . import models


class ProduitForm(ModelForm):
    class Meta:
        model = models.Produit
        fields = ('nom', 'prix', 'taille', 'description', 'avis', 'categorie')
        labels = {
            'nom': ('Nom'),
            'prix': ('Prix en Euro'),
            'taille': ('Taille en cm'),
            'description': ('Description'),
            'avis': ('Avis'),
            'categorie' : ('Categorie'),
        }
class CategorieForm(ModelForm):
    class Meta:
        model = models.Categorie
        fields = ('nom', 'description')
        labels = {
            'nom' : ('Nom'),
            'description' : ('Description'),
        }