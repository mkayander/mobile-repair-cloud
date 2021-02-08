import os

from django.urls import path

from project import settings
from . import views

urlpatterns = [
    path('', views.landing_page),
]

if not settings.DEBUG:
    urlpatterns += path('pwabuilder-sw.js', views.StaticFileView.as_view(source=os.path.join("js", "pwa.js")))
