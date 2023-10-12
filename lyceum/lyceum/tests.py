from django.test import Client, TestCase, override_settings


class StaticUrlTests(TestCase):
    @override_settings(ALLOW_REVERSE=True)
    def test_allow_true_middleware(self):
        responses_con = [Client().get("/about/").content for _ in range(11)]
        rez = [1 if el == responses_con[0] else 0 for el in responses_con]
        self.assertEqual(all(rez), False)

    @override_settings(ALLOW_REVERSE=False)
    def test_allow_false_middleware(self):
        responses_con = [Client().get("/catalog/").content for _ in range(11)]
        rez = [1 if el == responses_con[0] else 0 for el in responses_con]
        self.assertEqual(all(rez), True)

    @override_settings(ALLOW_REVERSE=True)
    def test_reverse_middleware(self):
        responses_con = [Client().get("/coffee/").content for _ in range(11)]
        rez = [1 if el == "Я кинйач".encode() else 0 for el in responses_con]
        self.assertEqual(any(rez), True)
