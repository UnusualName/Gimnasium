from django.test import Client, TestCase


class StaticUrlTests(TestCase):
    def test_catalog_endpoint(self):
        response = Client().get("/catalog/")
        self.assertEqual(response.status_code, 200)

    def test_catalog_item_endpoint(self):
        response = Client().get("/catalog/1234/")
        self.assertEqual(response.status_code, 200)

    def test_catalog_regular_positive_endpoint(self):
        response = Client().get("/catalog/re/-1234/")
        self.assertEqual(response.status_code, 404)

    def test_catalog_regular_text_endpoint(self):
        response = Client().get("/catalog/re/12r34/")
        self.assertEqual(response.status_code, 404)

    def test_catalog_converter_positive_endpoint(self):
        response = Client().get("/catalog/re/-1234/")
        self.assertEqual(response.status_code, 404)

    def test_catalog_converter_text_endpoint(self):
        response = Client().get("/catalog/re/12r34/")
        self.assertEqual(response.status_code, 404)
