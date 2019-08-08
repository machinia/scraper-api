from django.test import SimpleTestCase


class HeartbeatTest(SimpleTestCase):

    def test_heartbeat(self):
        resp = self.client.get("/heartbeat")
        self.assertEqual(resp.status_code, 200)
        self.assertJSONEqual(resp.content, {"status": "OK"})
