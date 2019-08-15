from django.http import JsonResponse

SPIDERS = [{
    "name": "amazon-whishlist",
    "version": "0.1.0",
    "description": "scrape public Amazon whishlist",
    "params": [{
        "name": "url",
        "type": "string",
        "description": "Amazon whishlist URL to be scraped",
    }]
}]


def spiders(request):
    return JsonResponse({"data": SPIDERS})
