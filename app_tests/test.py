import unittest
from web import app


class ApplicationTest(unittest.TestCase):

    def setUp(self):
        self.client = app.test_client()

    def test_healthcheck(self):
        resp = self.client.get("/healthcheck")
        self.assertTrue(resp.status_code == 200)
        self.assertTrue(resp.get_data() == b'{"status":"all good"}\n')

    def test_healthcheck(self):
        resp = self.client.post("/calc", {})
        self.assertTrue(resp.status_code == 200)
        self.assertTrue(resp.get_data() == b'{"status":"all good"}\n')


if __name__ == "__main__":
    unittest.main()
