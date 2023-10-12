from re import findall

from django.conf import settings

from . import settings as st


class SimpleMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        # Code to be executed for each request before
        # the view (and later middleware) are called.
        response = self.get_response(request)
        # Code to be executed for each request/response after
        # the view is called.
        if settings.ALLOW_REVERSE:
            st.times += 1
            if st.times % 10 == 0:
                unchanged_content = response.content.decode()
                changed_content = " ".join(
                    [
                        el[::-1]
                        for el in findall(r"[а-яА-ЯёЁ]+", unchanged_content)
                    ]
                )
                changed_content = changed_content.encode()
                if "<body>" in unchanged_content:
                    changed_content = b"<body>" + changed_content + b"</body>"
                response.content = changed_content
            # response
        return response
