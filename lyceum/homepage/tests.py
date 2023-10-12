from django.test import Client, TestCase


class StaticUrlTests(TestCase):
    def test_homepage_endpoint(self):
        response = Client().get("/")
        self.assertEqual(response.status_code, 200)

    def test_coffee_status_endpoint(self):
        response = Client().get("/coffee/")
        self.assertEqual(response.status_code, 418)

    def test_coffee_text_endpoint(self):
        response = Client().get("/coffee/")
        self.assertEqual(
            response.content,
            b"\xd0\xaf \xd1\x87\xd0\xb0\xd0\xb9\xd0\xbd\xd0\xb8\xd0\xba",
        )
