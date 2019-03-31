import unittest
import json
from web import app


class ApplicationTest(unittest.TestCase):

    def setUp(self):
        self.client = app.test_client()

    def test_healthcheck(self):
        resp = self.client.get("/healthcheck")
        self.assertTrue(resp.status_code == 200)
        self.assertTrue(resp.get_data() == b'{"status":"all good"}\n')

    def test_calculation(self):
        resp = self.client.post("/calc", data=json.dumps({
            "equation": "1/2 + 1/2"
        }), content_type="application/json")
        self.assertTrue(resp.status_code == 200)
        self.assertTrue(resp.get_data() == b'{"equation":"1/2 + 1/2","result":"1"}\n')

    def test_calculation1(self):
        resp = self.client.post("/calc", data=json.dumps({
            "equation": "2+1*1/2"
        }), content_type="application/json")
        self.assertTrue(resp.status_code == 200)
        self.assertTrue(resp.get_data() == b'{"equation":"2+1*1/2","result":"5/2"}\n')

    def test_invalid_expr(self):
        resp = self.client.post("/calc", data=json.dumps({
            "equation": "1/2 - 1/2("
        }), content_type="application/json")
        self.assertTrue(resp.status_code == 400)
        self.assertTrue(resp.get_data() == b'{"error":"Not allowed symbols or sequence"}\n')

    def test_invalid_expr1(self):
        resp = self.client.post("/calc", data=json.dumps({
            "equation": "1/5 + 1/5 + "
        }), content_type="application/json")
        self.assertTrue(resp.status_code == 400)
        self.assertTrue(resp.get_data() == b'{"error":"Not allowed symbols or sequence"}\n')

    def test_invalid_content_type(self):
        resp = self.client.post("/calc", data=json.dumps({
            "equation": "1/5 + 1/5 + "
        }), content_type="text/plain")
        self.assertTrue(resp.status_code == 400)


if __name__ == "__main__":
    unittest.main()
