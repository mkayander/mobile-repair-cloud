from django.contrib import admin

from web.models import Visitor, FeedbackRequest


@admin.register(Visitor)
class VisitorAdmin(admin.ModelAdmin):
    list_display = ["session", "user_agent", "visit_count", "last_visit", "created_at"]


@admin.register(FeedbackRequest)
class FeedbackRequestAdmin(admin.ModelAdmin):
    list_display = ["visitor", "phone", "email", "subject"]
