import json
from django.http import JsonResponse

import scraper_factory

SPIDERS = [{
    "name": "amazon-wishlist",
    "version": "0.1.0",
    "description": "scrape public Amazon wishlist",
    "params": [{
        "name": "url",
        "type": "string",
        "description": "Amazon wishlist URL to be scraped",
    }]
}]


def spiders(request):
    return JsonResponse({"data": SPIDERS})


def scrape(request, spider_name):
    if spider_name != "amazon-wishlist":
        return JsonResponse({"error": "'%s': spider not found" % spider_name})

    body = json.loads(request.body)
    url = body.get("url")
    print(request.body)
    if not url:
        return JsonResponse({"error": "'url' key not found"})

    resp = scraper_factory.scrape(url)
    return JsonResponse({"data": resp})
