from django.shortcuts import render, HttpResponseRedirect
from .forms import ProduitForm
from . import models


# Create your views here.
def produit(request):
    if request.method == "POST":
        form = ProduitForm(request)
        return render(request, "store/produit.html", {"form": form})
    else:
        form = ProduitForm()
        return render(request, "store/produit.html", {"form": form})


def traitement(request):
    pform = ProduitForm(request.POST)
    if pform.is_valid():
        produit = pform.save()
        return HttpResponseRedirect("/store/")
    else:
        return render(request, "store/produit.html", {"form": pform})


def index(request):
    liste = list(models.Produit.objects.all())
    return render(request, "store/index.html", {"liste": liste})


def infos(request, id):
    produit = models.Produit.objects.get(pk=id)
    return render(request, "store/infos.html", {"produit": produit})


def update(request, id):
    produit = models.Produit.objects.get(pk=id)
    form = ProduitForm(produit.dico())
    return render(request, "store/produit.html", {"form": form, "id": id})


def updatetraitement(request, id):
    pform = ProduitForm(request.POST)
    if pform.is_valid():
        produit = pform.save(commit=False)
        produit.id = id
        produit.save()
        return HttpResponseRedirect("/store/")
    else:
        return render(request, "store/produit.html", {"form": pform, "id": id})


def delete(request, id):
    produit = models.Produit.objects.get(pk=id)
    produit.delete()
    return HttpResponseRedirect("/store/")
