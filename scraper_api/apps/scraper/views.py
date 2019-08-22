import json
from django.http import JsonResponse

import scraper_factory
from scraper_factory.core.exceptions import InvalidUrlError
from scraper_factory.core.exceptions import SpiderNotFoundError


def spiders(request):
    return JsonResponse({"data": scraper_factory.spiders()})


def scrape(request, spider_name):
    body = request.body
    if not body:
        return JsonResponse({"error": "JSON data required"}, status=400)

    kwargs = json.loads(request.body)

    try:
        resp = scraper_factory.scrape(spider_name, **kwargs)
        return JsonResponse({"data": resp})

    except SpiderNotFoundError as e:
        return JsonResponse({"error": str(e)}, status=404)

    except InvalidUrlError as e:
        return JsonResponse({"error": str(e)}, status=400)

    except TypeError as e:
        return JsonResponse({"error": str(e)}, status=400)

    except Exception as e:
        return JsonResponse({"error": str(e)}, status=500)
