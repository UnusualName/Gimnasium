from unittest.mock import MagicMock

from django.test import Client, override_settings, TestCase
from parameterized import parameterized

from .middleware import SimpleMiddleware


class StaticUrlTests(TestCase):
    @parameterized.expand([
        ("Я чайник", "Я кинйач"),
        ("zzzРаз0tre", "zzzзаР0tre"),
        ("Привет, мир!", "тевирП, рим!"),
        ("АБВОовапу арак fffff", "упавоОВБА кара fffff"),
        ("Hello, world!", "Hello, world!"),
    ])
    @override_settings(ALLOW_REVERSE=True)
    def test_positive_middleware(self, text, excepted):
        get_response = MagicMock()
        get_response.return_value.content = text.encode()
        request = Client().get("/")

        middleware = SimpleMiddleware(get_response)
        responses = [middleware(request) for _ in range(10)]

        # ensure get_response has been returned
        # (or not, if your middleware does something else)

        self.assertEqual(excepted, responses[-1].content.decode())

    @parameterized.expand([
        ("Я чайник", "Я кинйач"),
        ("zzzРаз0tre", "zzzзаР0tre"),
        ("Привет, мир!", "тевирП, рим!"),
        ("АБВОовапу арак fffff", "упавоОВБА кара fffff"),
    ])
    @override_settings(ALLOW_REVERSE=False)
    def test_negative_allowe_middleware(self, text, excepted):
        get_response = MagicMock()
        get_response.return_value.content = text.encode()
        request = Client().get("/")

        middleware = SimpleMiddleware(get_response)
        responses = [middleware(request) for _ in range(10)]

        # ensure get_response has been returned
        # (or not, if your middleware does something else)

        self.assertNotEqual(excepted, responses[-1].content.decode())
