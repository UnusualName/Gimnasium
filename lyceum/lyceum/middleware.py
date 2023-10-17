import re

from django.conf import settings


class SimpleMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response
        self.time = 0

    def __call__(self, request):
        self.time += 1
        response = self.get_response(request)

        if self.time % 10 == 0 and settings.ALLOW_REVERSE:
            unchanged_content = response.content.decode()
            out_con = ""
            end_index = 0
            for iter in re.finditer(r"[а-яА-ЯёЁ]+", unchanged_content):
                out_con += unchanged_content[
                    end_index : iter.start()  # noqa E203
                ]
                out_con += iter[0][::-1]
                end_index = iter.end()
            out_con += unchanged_content[end_index:]
            out_con = out_con.encode()
            response.content = out_con
        return response
