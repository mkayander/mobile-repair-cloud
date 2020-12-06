from django.urls import path, include
from rest_framework import routers

from . import views

router = routers.DefaultRouter()
router.register('visitors', views.VisitorViewSet)
router.register('feedback-requests', views.FeedbackRequestViewSet)

urlpatterns = [
    path('', include(router.urls), name="api_root"),
    path('action/get-identity', views.acquire_visitor_identity)
]
