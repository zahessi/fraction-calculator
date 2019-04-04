import json
import unittest

from web import app


class ApplicationTest(unittest.TestCase):

    def setUp(self):
        self.client = app.test_client()

    def test_healthcheck(self):
        resp = self.client.get("/healthcheck")
        self.assertTrue(resp.status_code == 200)
        self.assertTrue(resp.get_data() == b'status\tall good')

    def test_calculation(self):
        resp = self.client.post("/calc", data=json.dumps({
            "equation": "1/2 + 1/2"
        }), content_type="application/json")
        self.assertTrue(resp.status_code == 200)
        self.assertTrue(resp.get_data() == b'equation\t1/2 + 1/2\nresult\t1')

    def test_calculation1(self):
        resp = self.client.post("/calc", data=json.dumps({
            "equation": "2+1*1/2"
        }), content_type="application/json")
        self.assertTrue(resp.status_code == 200)
        self.assertTrue(resp.get_data() == b'equation\t2+1*1/2\nresult\t5/2')

    def test_calculation_with_text_plain(self):
        resp = self.client.post("/calc", data="equation\t2+1*1/2", content_type="text/plain")
        print(resp.get_data())
        self.assertTrue(resp.status_code == 200)
        self.assertTrue(resp.get_data() == b'equation\t2+1*1/2\nresult\t5/2')

    def test_invalid_expr(self):
        resp = self.client.post("/calc", data=json.dumps({
            "equation": "1/2 - 1/2("
        }), content_type="application/json")
        self.assertTrue(resp.status_code == 400)
        self.assertTrue(resp.get_data() == b'equation\t1/2 - 1/2(\nerror\tNot allowed symbols or sequence')

    def test_invalid_expr1(self):
        resp = self.client.post("/calc", data=json.dumps({
            "equation": "1/5 + 1/5 + "
        }), content_type="application/json")
        self.assertTrue(resp.status_code == 400)
        self.assertTrue(resp.get_data() == b'equation\t1/5 + 1/5 + \nerror\tNot allowed symbols or sequence')

    def test_invalid_content_type(self):
        resp = self.client.post("/calc", data=json.dumps({
            "equation": "1/5 + 1/5 + "
        }), content_type="text/plain")
        self.assertTrue(resp.status_code == 400)


if __name__ == "__main__":
    unittest.main()
