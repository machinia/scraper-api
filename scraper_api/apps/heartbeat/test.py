from django.test import SimpleTestCase


class HeartbeatTest(SimpleTestCase):

    def test_heartbeat(self):
        resp = self.client.get("/heartbeat/")
        self.assertEqual(resp.status_code, 200)
        self.assertJSONEqual(resp.content, {"status": "OK"})

    def test_heartbeat_redirect(self):
        resp = self.client.get("/heartbeat")
        self.assertRedirects(resp, "/heartbeat/", 301, 200)
