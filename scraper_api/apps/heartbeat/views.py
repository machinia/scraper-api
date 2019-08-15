from django.http import JsonResponse


def heartbeat(request):
    return JsonResponse({"status": "OK"})
