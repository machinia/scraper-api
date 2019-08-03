from django.urls import path
from scraper_api.app.views import heartbeat


urlpatterns = [
    path("", heartbeat, name="heartbeat"),
]
