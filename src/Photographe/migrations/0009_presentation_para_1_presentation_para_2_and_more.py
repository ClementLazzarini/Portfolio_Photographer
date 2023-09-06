# Generated by Django 4.2.4 on 2023-08-31 12:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Photographe', '0008_remove_tarif_review_tarif_description'),
    ]

    operations = [
        migrations.AddField(
            model_name='presentation',
            name='para_1',
            field=models.TextField(blank=True, max_length=1000, verbose_name='Paragraphe 1'),
        ),
        migrations.AddField(
            model_name='presentation',
            name='para_2',
            field=models.TextField(blank=True, max_length=1000, verbose_name='Paragraphe 2'),
        ),
        migrations.AddField(
            model_name='presentation',
            name='signature',
            field=models.CharField(blank=True, max_length=100, verbose_name='Signature'),
        ),
    ]