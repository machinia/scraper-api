from unittest import mock
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

    def test_scrape_wrong_spider_name(self):
        resp = self.client.post("/api/v1/spider/wrong-spider-name")
        self.assertEqual(resp.status_code, 200)
        expected = {"error": "'wrong-spider-name': spider not found"}
        self.assertJSONEqual(resp.content, expected)

    def test_scrape_url_not(self):
        resp = self.client.post("/api/v1/spider/amazon-whishlist",
                                data={},
                                content_type="application/json")
        self.assertEqual(resp.status_code, 200)
        self.assertJSONEqual(resp.content, {"error": "'url' key not found"})

    def test_scrape_url_wrong(self):
        resp = self.client.post("/api/v1/spider/amazon-whishlist",
                                data={"url": "wrong-url"},
                                content_type="application/json")
        self.assertEqual(resp.status_code, 200)
        self.assertJSONEqual(resp.content, {"data": []})

    @mock.patch("scraper_factory.scrape")
    def test_scrape_spider(self, scrape):
        return_value = [
            {"id": 1, "desc": "desc from obj 1 from web page"},
            {"id": 2, "desc": "desc from obj 2 from web page"},
        ]
        scrape.return_value = return_value

        resp = self.client.post("/api/v1/spider/amazon-whishlist",
                                data={"url": "some-url"},
                                content_type="application/json")
        self.assertEqual(resp.status_code, 200)
        self.assertJSONEqual(resp.content, {"data": return_value})
