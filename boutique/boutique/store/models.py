from django.db import models


# Create your models here.
class Produit(models.Model):
    nom = models.CharField(max_length=100)
    prix = models.IntegerField(blank=False)
    taille = models.IntegerField(blank=False)
    description = models.TextField(null=True, blank=True)
    avis = models.TextField(null=True, blank=True)
    categorie = models.ForeignKey("categorie", on_delete=models.CASCADE, default=None)

    def __str__(self):
        chaine = f"nom: {self.nom} prix: {self.prix} taille: {self.taille}"
        return chaine

    def dico(self):
        return {"nom": self.nom, "prix": self.prix, "taille": self.taille, "description": self.description, "avis": self.avis, "categorie": self.categorie}


class Categorie(models.Model):
    nom = models.CharField(max_length=100)
    description = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.nom

    def dico(self):
        return{"nom": self.nom, "description": self.description}