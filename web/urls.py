import os

from django.urls import path

from . import views

urlpatterns = [
    path('', views.landing_page),
    path('pwabuilder-sw.js', views.StaticFileView.as_view(source=os.path.join("js", "pwa.js")))
    # path('api/', include('api.urls'))
]
