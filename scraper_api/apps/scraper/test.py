import json
from unittest import mock
from django.test import SimpleTestCase


class SpiderTest(SimpleTestCase):

    def test_spider(self):
        resp = self.client.get("/api/v1/spider/")
        self.assertEqual(resp.status_code, 200)
        resp = json.loads(resp.content)
        self.assertTrue(isinstance(resp, dict))
        self.assertTrue(isinstance(resp["data"], list))

    def test_spider_redirect(self):
        resp = self.client.get("/api/v1/spider")
        self.assertRedirects(resp, "/api/v1/spider/", 301, 200)

    def test_scrape_wrong_spider_name(self):
        name = "wrong-spider-name"
        resp = self.client.post("/api/v1/spider/%s" % name,
                                content_type="application/json")
        self.assertEqual(resp.status_code, 404)
        expected = {"error": "Spider %s doesn't exist" % name}
        self.assertJSONEqual(resp.content, expected)

    def test_scrape_no_data(self):
        resp = self.client.get("/api/v1/spider/amazon-wishlist",
                               content_type="application/json")
        self.assertEqual(resp.status_code, 400)
        self.assertJSONEqual(resp.content, {"error": "JSON data required"})

    def test_scrape_url_not(self):
        resp = self.client.post("/api/v1/spider/amazon-wishlist",
                                data={},
                                content_type="application/json")
        self.assertEqual(resp.status_code, 400)
        error = "__init__() missing 1 required positional argument: 'url'"
        self.assertJSONEqual(resp.content, {"error": error})

    def test_scrape_url_wrong(self):
        resp = self.client.post("/api/v1/spider/amazon-wishlist",
                                data={"url": "wrong-url"},
                                content_type="application/json")
        self.assertEqual(resp.status_code, 400)
        self.assertJSONEqual(resp.content, {"error": "Invalid URL"})

    @mock.patch("scraper_factory.scrape", side_effect=RuntimeError("Test"))
    def test_scrape_any_exception(self, scrape):
        resp = self.client.post("/api/v1/spider/amazon-wishlist",
                                data={"url": "some-url"},
                                content_type="application/json")
        self.assertEqual(resp.status_code, 500)
        self.assertJSONEqual(resp.content, {"error": "Test"})

    @mock.patch("scraper_factory.scrape")
    def test_scrape_spider(self, scrape):
        return_value = [
            {"id": 1, "desc": "desc from obj 1 from web page"},
            {"id": 2, "desc": "desc from obj 2 from web page"},
        ]
        scrape.return_value = return_value

        resp = self.client.post("/api/v1/spider/amazon-wishlist",
                                data={"url": "some-url"},
                                content_type="application/json")
        self.assertEqual(resp.status_code, 200)
        self.assertJSONEqual(resp.content, {"data": return_value})
