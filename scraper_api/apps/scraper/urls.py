from django.urls import path
from scraper_api.apps.scraper.views import spiders


urlpatterns = [
    path("", spiders, name="spiders"),
]
