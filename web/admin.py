from django.contrib import admin

from web.models import Visitor, FeedbackRequest, GalleryPhoto


@admin.register(Visitor)
class VisitorAdmin(admin.ModelAdmin):
    list_display = ["ip_address", "session", "user_agent", "visit_count", "last_visit", "created_at"]
    ordering = ["-last_visit"]


@admin.register(FeedbackRequest)
class FeedbackRequestAdmin(admin.ModelAdmin):
    list_display = ["subject", "phone", "email", "message", "visitor"]


@admin.register(GalleryPhoto)
class GalleryPhotoAdmin(admin.ModelAdmin):
    list_display = ["description", "created_at", "image", "id"]
