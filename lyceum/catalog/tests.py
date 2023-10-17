from http import HTTPStatus

from django.test import Client, TestCase
from parameterized import parameterized


class StaticUrlTests(TestCase):
    @parameterized.expand(
        [
            ("", HTTPStatus.OK),
            ("/1234", HTTPStatus.OK),
            ("/1", HTTPStatus.OK),
            ("/re/1", HTTPStatus.OK),
            ("/re/1234", HTTPStatus.OK),
            ("/converter/1", HTTPStatus.OK),
            ("/converter/1234", HTTPStatus.OK),
        ]
    )
    def test_catalog_positive_endpoint(self, item, excepted):
        response = Client().get(f"/catalog{item}/")
        self.assertEqual(response.status_code, excepted)

    @parameterized.expand(
        [
            ("/text", HTTPStatus.NOT_FOUND),
            ("/o", HTTPStatus.NOT_FOUND),
            ("/re/12r34", HTTPStatus.NOT_FOUND),
            ("/re/0", HTTPStatus.NOT_FOUND),
            ("/re/-1", HTTPStatus.NOT_FOUND),
            ("/converter/12r34", HTTPStatus.NOT_FOUND),
            ("/converter/0", HTTPStatus.NOT_FOUND),
            ("/converter/-1", HTTPStatus.NOT_FOUND),
        ]
    )
    def test_catalog_negative_endpoint(self, item, excepted):
        response = Client().get(f"/catalog{item}/")
        self.assertEqual(response.status_code, excepted)
