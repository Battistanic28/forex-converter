from unittest import TestCase
from app import app


class ForexTestCase(TestCase):
    def test_convert(self):
        with app.test_client as client:
            res = client.get('/')
            html = res.get_data(as_text=True)

            self.assertEqual(res.status_code, 200)
            self.assertIn('<h1 class="text-center m-3">Forex Converter</h1>', html)