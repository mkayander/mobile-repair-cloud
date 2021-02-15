from django.contrib import admin
from django.utils.translation import gettext_lazy as _

# Register your models here.
from imagekit.admin import AdminThumbnail

from pricing.models import Brand, DeviceModel, Service


@admin.register(Brand)
class BrandAdmin(admin.ModelAdmin):
    image_display = AdminThumbnail(image_field='logo', template="admin_thumbnail.html")
    image_display.short_description = _('Logo display')

    list_display = ['name', 'image_display']
    readonly_fields = ['image_display']  # this is for the change form


@admin.register(DeviceModel)
class DeviceModelAdmin(admin.ModelAdmin):
    pass


@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    pass
