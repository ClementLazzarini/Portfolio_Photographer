from django.db import models
from PIL import Image


class Category(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Portfolio(models.Model):
    MEDIA_TYPES = (
        ('photo', 'Photo'),
        ('video', 'Video'),
    )

    title = models.CharField(max_length=100, verbose_name="Nom")
    media_type = models.CharField(max_length=10, choices=MEDIA_TYPES, verbose_name="Type de contenu")
    file = models.FileField(blank=True, null=True, verbose_name="Vidéo")
    thumbnail = models.ImageField(blank=True, verbose_name="Image")
    uploaded_at = models.DateTimeField(auto_now_add=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name="Catégorie")

    def __str__(self):
        return self.title


class Homeslide(models.Model):
    title = models.CharField(max_length=100, verbose_name="Nom")
    thumbnail = models.ImageField(blank=True, verbose_name="Image")
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class Homecard(models.Model):
    title = models.CharField(max_length=100, verbose_name="Nom")
    thumbnail = models.ImageField(blank=True, verbose_name="Image")

    def __str__(self):
        return self.title


class Homereview(models.Model):
    title = models.CharField(max_length=100, verbose_name="Nom")
    thumbnail = models.ImageField(blank=True, verbose_name="Image")
    review = models.TextField(verbose_name="Avis")

    def __str__(self):
        return self.title


class Presentation(models.Model):
    thumbnail = models.ImageField(blank=True, verbose_name="Image")
    para_1 = models.TextField(max_length=1000, blank=True, verbose_name="Paragraphe 1")
    para_2 = models.TextField(max_length=1000, blank=True, verbose_name="Paragraphe 2")
    signature = models.CharField(max_length=100, blank=True, verbose_name="Signature")

    def __str__(self):
        return "Présentation"


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
