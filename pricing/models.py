from django.db import models
# Create your models here.
from djmoney.models.fields import MoneyField

from pricing.validators import validate_svg


class Brand(models.Model):
    name = models.TextField(verbose_name="Наименование", max_length=64)
    logo = models.FileField(verbose_name="Логотип", help_text="Требуемый формат - *.svg", upload_to="svg_logos/",
                            validators=[validate_svg])

    class Meta:
        verbose_name = "Брэнд устройства"
        verbose_name_plural = "Брэнды устройств"


class DeviceModel(models.Model):
    name = models.TextField(verbose_name="Наименование", max_length=64)
    brand = models.ForeignKey(Brand, verbose_name="Брэнд", on_delete=models.CASCADE, related_name="models")

    class Meta:
        verbose_name = "Модель устройства"
        verbose_name_plural = "Модели устройств"


class Service(models.Model):
    name = models.TextField(verbose_name="Наименование", max_length=128)
    model = models.ForeignKey(DeviceModel, verbose_name="Модель устройства", on_delete=models.CASCADE,
                              related_name="services")
    price = MoneyField(verbose_name="Стоимость", max_digits=8, decimal_places=2, default_currency='RUB', null=True)

    class Meta:
        verbose_name = "Услуга"
        verbose_name_plural = "Услуги"
