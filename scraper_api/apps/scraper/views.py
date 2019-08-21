import json
from django.http import JsonResponse

import scraper_factory


def spiders(request):
    return JsonResponse({"data": scraper_factory.spiders()})


def scrape(request, spider_name):
    if spider_name != "amazon-wishlist":
        return JsonResponse({"error": "'%s': spider not found" % spider_name},
                            status=404)

    body = json.loads(request.body)
    url = body.get("url")
    print(request.body)
    if not url:
        return JsonResponse({"error": "'url' key not found"}, status=400)

    resp = scraper_factory.scrape(url)
    return JsonResponse({"data": resp})
