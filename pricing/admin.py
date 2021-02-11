from django.contrib import admin

# Register your models here.
from pricing.models import Brand, DeviceModel, Service


@admin.register(Brand)
class BrandAdmin(admin.ModelAdmin):
    pass


@admin.register(DeviceModel)
class DeviceModelAdmin(admin.ModelAdmin):
    pass


@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    pass
