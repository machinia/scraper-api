from django.urls import include
from django.urls import path

urlpatterns = [
    path("heartbeat", include("scraper_api.app.urls")),
]
