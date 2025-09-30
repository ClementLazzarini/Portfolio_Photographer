from django.contrib import admin
from Photographe.models import Category, Portfolio, Homeslide, Homecard, Homereview, Presentation, Tarif


class CategoryAdmin(admin.ModelAdmin):
    list_display = ("name", )


class PortfolioAdmin(admin.ModelAdmin):
    list_display = ("title", "category", "media_type", "uploaded_at")


class HomeslideAdmin(admin.ModelAdmin):
    list_display = ("title", "uploaded_at")


class HomecardAdmin(admin.ModelAdmin):
    list_display = ("title", )


class HomereviewAdmin(admin.ModelAdmin):
    list_display = ("title", )


class PresentationAdmin(admin.ModelAdmin):
    list_display = ("thumbnail", )


class TarifAdmin(admin.ModelAdmin):
    list_display = ("title", "price")


admin.site.register(Category, CategoryAdmin)
admin.site.register(Portfolio, PortfolioAdmin)
admin.site.register(Homeslide, HomeslideAdmin)
admin.site.register(Homecard, HomecardAdmin)
admin.site.register(Homereview, HomereviewAdmin)
admin.site.register(Presentation, PresentationAdmin)
admin.site.register(Tarif, TarifAdmin)
