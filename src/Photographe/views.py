from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from Photographe.models import Portfolio, Homeslide, Homecard, Homereview, Presentation, Tarif, Category


def home(request):
    mediaslides = Homeslide.objects.all()
    mediacards = Homecard.objects.all()
    mediareviews = Homereview.objects.all()

    return render(request, "Photographe/index.html", {"mediaslides": mediaslides,
                                                      "mediacards": mediacards,
                                                      "mediareviews": mediareviews})


def portfolio(request):
    categories = Category.objects.all()
    selected_category = request.GET.get('category')

    if selected_category:
        category = get_object_or_404(Category, name=selected_category)
        medias = Portfolio.objects.filter(category=category)
    else:
        medias = Portfolio.objects.all()

    return render(request, "Photographe/portfolio.html", {"medias": medias,
                                                          "categories": categories,
                                                          "selected_category": selected_category})


def tarif(request):
    tarifs = Tarif.objects.all()

    return render(request, "Photographe/tarif.html", {"tarifs": tarifs})


def presentation(request):
    presentations = Presentation.objects.all()

    return render(request, "Photographe/presentation.html", {"presentations": presentations})


def contact(request):
    # Récupérer la liste complète des produits
    medias = Portfolio.objects.all()

    return render(request, "Photographe/contact.html", {"medias": medias})


def mentions(request):
    # Récupérer la liste complète des produits
    medias = Portfolio.objects.all()

    return render(request, "Photographe/mentions.html", {"medias": medias})
