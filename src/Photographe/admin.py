from django.contrib import admin
from Photographe.models import Category, Portfolio, Homeslide, Homecard, Homereview, Presentation, Tarif


# 🖼️ --- GALERIE ---
@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ("name", )
    verbose_name = "Catégorie"
    verbose_name_plural = "Catégories"


@admin.register(Portfolio)
class PortfolioAdmin(admin.ModelAdmin):
    list_display = ("title", "category", "media_type", "uploaded_at")
    verbose_name = "Portfolio"
    verbose_name_plural = "Portfolios"


# 🏠 --- PAGE D’ACCUEIL ---
@admin.register(Homeslide)
class HomeslideAdmin(admin.ModelAdmin):
    list_display = ("title", "uploaded_at")
    verbose_name = "Diaporama d'accueil"
    verbose_name_plural = "Diaporamas d'accueil"


@admin.register(Homecard)
class HomecardAdmin(admin.ModelAdmin):
    list_display = ("title", )
    verbose_name = "Carte d'accueil"
    verbose_name_plural = "Cartes d'accueil"


@admin.register(Homereview)
class HomereviewAdmin(admin.ModelAdmin):
    list_display = ("title", )
    verbose_name = "Avis client"
    verbose_name_plural = "Avis clients"


# 👤 --- PRÉSENTATION ---
@admin.register(Presentation)
class PresentationAdmin(admin.ModelAdmin):
    list_display = ("thumbnail", )
    verbose_name = "Présentation"
    verbose_name_plural = "Présentation"


# 💰 --- TARIFS ---
@admin.register(Tarif)
class TarifAdmin(admin.ModelAdmin):
    list_display = ("title", "price")
    verbose_name = "Tarif"
    verbose_name_plural = "Tarifs"


# 🧭 --- PERSONNALISATION DE L’ADMIN ---
admin.site.site_header = "Administration du site photographe"
admin.site.site_title = "Site Photographe"
admin.site.index_title = "Tableau de bord"
