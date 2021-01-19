from django.db import models


class LandingPhoto(models.Model):
    image = models.ImageField(verbose_name="Файл фотографии")
