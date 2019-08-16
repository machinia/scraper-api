from django.urls import path
from scraper_api.apps.scraper.views import scrape
from scraper_api.apps.scraper.views import spiders


urlpatterns = [
    path("", spiders, name="spiders"),
    path("<str:spider_name>", scrape, name="scrape"),
]
