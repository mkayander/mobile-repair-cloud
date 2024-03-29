from django.db import models
# Create your models here.
from djmoney.models.fields import MoneyField

from pricing.validators import validate_svg


class Brand(models.Model):
    name = models.CharField(verbose_name="Наименование", max_length=64, unique=True)
    logo = models.FileField(verbose_name="Логотип", help_text="Требуемый формат - *.svg", upload_to="svg_logos/",
                            validators=[validate_svg])

    class Meta:
        verbose_name = "Брэнд устройства"
        verbose_name_plural = "Брэнды устройств"
        ordering = ["name"]

    def __str__(self):
        return self.name


class DeviceModel(models.Model):
    name = models.CharField(verbose_name="Наименование", max_length=64)
    brand = models.ForeignKey(Brand, verbose_name="Брэнд", on_delete=models.CASCADE, related_name="models")

    class Meta:
        verbose_name = "Модель устройства"
        verbose_name_plural = "Модели устройств"
        constraints = [
            models.UniqueConstraint(fields=["name", "brand"], name="unique_device_model")
        ]
        ordering = ["brand", "name"]

    def __str__(self):
        return f"{self.brand} {self.name}"


class Service(models.Model):
    name = models.CharField(verbose_name="Наименование", max_length=128)
    model = models.ForeignKey(DeviceModel, verbose_name="Модель устройства", on_delete=models.CASCADE,
                              related_name="services")
    price = MoneyField(verbose_name="Стоимость", max_digits=8, decimal_places=2, default_currency='RUB', null=True)

    class Meta:
        verbose_name = "Услуга"
        verbose_name_plural = "Услуги"
        constraints = [
            models.UniqueConstraint(fields=["name", "model"], name="unique_device_service")
        ]
        ordering = ["model", "name"]

    def __str__(self):
        return f"{self.model} {self.name}"
