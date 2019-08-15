from django.test import SimpleTestCase
from scraper_api.apps.scraper.views import SPIDERS


class SpiderTest(SimpleTestCase):

    def test_spider(self):
        resp = self.client.get("/api/v1/spider/")
        self.assertEqual(resp.status_code, 200)
        self.assertJSONEqual(resp.content, {"data": SPIDERS})

    def test_spider_redirect(self):
        resp = self.client.get("/api/v1/spider")
        self.assertRedirects(resp, "/api/v1/spider/", 301, 200)
