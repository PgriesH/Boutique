from django.shortcuts import render, HttpResponseRedirect
from .forms import CategorieForm
from . import models


# Create your views here.
def ajout(request):
    if request.method == "POST":
        form = CategorieForm(request)
        return render(request, "categorie/ajout.html", {"form": form})
    else:
        form = CategorieForm()
        return render(request, "categorie/ajout.html", {"form": form})


def traitement(request):
    lform = CategorieForm(request.POST)
    if lform.is_valid():
        categorie = lform.save()
        return HttpResponseRedirect("/store/indexcategorie/")
    else:
        return render(request, "categorie/ajout.html", {"form": lform})


def index(request):
    liste = list(models.Categorie.objects.all())
    return render(request, "categorie/index.html", {"liste": liste})


def affiche(request, id):
    categorie = models.Categorie.objects.get(pk=id)
    return render(request, "categorie/affiche.html", {"categorie": categorie})




def update(request, id):
    categorie = models.Categorie.objects.get(pk=id)
    form = CategorieForm(categorie.dico())
    return render(request, "categorie/ajout.html", {"form": form, "id": id})


def updatetraitement(request, id):
    lform = CategorieForm(request.POST)
    if lform.is_valid():
        categorie = lform.save(commit=False)
        categorie.id = id
        categorie.save()
        return HttpResponseRedirect("/store/")
    else:
        return render(request, "categorie/ajout.html", {"form": lform, "id": id})

def delete(request, id):
    categorie = models.Categorie.objects.get(pk=id)
    categorie.delete()
    return HttpResponseRedirect("/store/indexcategorie/")
