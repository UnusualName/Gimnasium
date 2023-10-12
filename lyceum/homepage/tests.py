from http import HTTPStatus

from django.test import Client, override_settings, TestCase


class StaticUrlTests(TestCase):
    def test_homepage_endpoint(self):
        response = Client().get("/")
        self.assertEqual(response.status_code, 200)

    def test_coffee_status_endpoint(self):
        response = Client().get("/coffee/")
        self.assertEqual(response.status_code, 418)

    def test_coffee_httpstatus_endpoint(self):
        response = Client().get("/coffee/")
        self.assertEqual(response.status_code, HTTPStatus.IM_A_TEAPOT)

    @override_settings(ALLOW_REVERSE=False)
    def test_coffee_text_endpoint(self):
        response = Client().get("/coffee/")
        self.assertEqual(
            response.content,
            "Я чайник".encode(),
        )
