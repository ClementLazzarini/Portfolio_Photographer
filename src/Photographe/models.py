from django.db import models
from django.core.exceptions import ValidationError
from PIL import Image


class Category(models.Model):
    name = models.CharField(max_length=50, help_text="Titre de la catégorie de photo")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Portfolio - Catégorie"
        verbose_name_plural = "Portfolio - Catégories"


class Portfolio(models.Model):
    MEDIA_CHOICES = (
        ("image", "Image"),
        ("video", "Vidéo"),
    )

    title = models.CharField("Titre", max_length=100)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name="Catégorie")
    media_type = models.CharField("Type de média", max_length=10, choices=MEDIA_CHOICES)
    image = models.ImageField("Image", upload_to="portfolio/images/", blank=True, null=True)
    video = models.FileField("Vidéo", upload_to="portfolio/videos/", blank=True, null=True)
    uploaded_at = models.DateTimeField("Date d'ajout", auto_now_add=True)

    class Meta:
        verbose_name = "Élément du portfolio"
        verbose_name_plural = "Portfolio"

    def __str__(self):
        return self.title

    def clean(self):
        """Empêche d’avoir une image et une vidéo en même temps, ou aucun des deux."""
        if self.image and self.video:
            raise ValidationError("⚠️ Tu ne peux pas ajouter à la fois une image et une vidéo.")
        if not self.image and not self.video:
            raise ValidationError("⚠️ Tu dois ajouter soit une image, soit une vidéo.")
        # Optionnel : cohérence avec media_type
        if self.media_type == "image" and not self.image:
            raise ValidationError("Tu as sélectionné 'Image' mais aucun fichier image n’a été ajouté.")
        if self.media_type == "video" and not self.video:
            raise ValidationError("Tu as sélectionné 'Vidéo' mais aucun fichier vidéo n’a été ajouté.")

    def save(self, *args, **kwargs):
        """Appelle la validation à chaque sauvegarde."""
        self.clean()
        super().save(*args, **kwargs)


class Homeslide(models.Model):
    title = models.CharField(max_length=100, verbose_name="Nom")
    thumbnail = models.ImageField(blank=True, verbose_name="Image")
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Accueil - Diaporama"
        verbose_name_plural = "Accueil - Diaporama"


class Homecard(models.Model):
    title = models.CharField(max_length=100, verbose_name="Nom")
    thumbnail = models.ImageField(blank=True, verbose_name="Image")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Accueil - Catégorie"
        verbose_name_plural = "Accueil - Catégories"


class Homereview(models.Model):
    title = models.CharField(max_length=100, verbose_name="Nom")
    thumbnail = models.ImageField(blank=True, verbose_name="Image")
    review = models.TextField(verbose_name="Avis")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Accueil - Avis Client"
        verbose_name_plural = "Accueil - Avis Clients"


class Presentation(models.Model):
    thumbnail = models.ImageField(blank=True, verbose_name="Image")
    para_1 = models.TextField(max_length=1000, blank=True, verbose_name="Paragraphe 1")
    para_2 = models.TextField(max_length=1000, blank=True, verbose_name="Paragraphe 2")
    signature = models.CharField(max_length=100, blank=True, verbose_name="Signature")

    def __str__(self):
        return "Présentation"

    class Meta:
        verbose_name = "Présentation"
        verbose_name_plural = "Présentation"


class Tarif(models.Model):
    title = models.CharField(max_length=100, verbose_name="Nom")
    thumbnail = models.ImageField(blank=True, verbose_name="Image")
    description = models.TextField(max_length=1000, blank=True, verbose_name="Description")
    time = models.CharField(max_length=100, verbose_name="Temps")
    pictures_nb = models.CharField(max_length=100, verbose_name="Nombre de photos")
    price = models.CharField(max_length=100, verbose_name="Prix")
    inverse = models.BooleanField(default=False, verbose_name="Inversé ?")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Tarif"
        verbose_name_plural = "Tarifs"
