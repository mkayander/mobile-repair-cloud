import os

from django.urls import path

from project import settings
from . import views

urlpatterns = [
    path('', views.landing_page),
]

