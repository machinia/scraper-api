from django.urls import path
from scraper_api.apps.heartbeat.views import heartbeat


urlpatterns = [
    path("", heartbeat, name="heartbeat"),
]
