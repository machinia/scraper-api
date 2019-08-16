from django.urls import include
from django.urls import path

urlpatterns = [
    path("heartbeat/", include("scraper_api.apps.heartbeat.urls")),
    path("api/v1/spider/", include("scraper_api.apps.scraper.urls")),
]
