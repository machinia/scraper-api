import os

ALLOWED_HOSTS = [
    "machinia-scraper-api.herokuapp.com",
]
DEBUG = os.environ.get("DJANGO_DEBUG", "") != "False"
MIDDLEWARE = [
    "django.middleware.common.CommonMiddleware",
]
ROOT_URLCONF = "scraper_api.urls"
SECRET_KEY = os.environ.get("DJANGO_SECRET_KEY",
                            "(a(!1*6lt*n0-wdkof*e)nnrmun)zrlbgeuul!%d+b2!%m4-k_")
WSGI_APPLICATION = "scraper_api.wsgi.application"
