from django.urls import path, include
from rest_framework import routers

from . import views

router = routers.DefaultRouter()
router.register('visitors', views.VisitorViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('action/get-identity', views.acquire_visitor_identity)
]
