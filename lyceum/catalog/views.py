from django.http import HttpResponse


def item_list(request):
    return HttpResponse("<body>Список элементов</body>")


def item_detail(request, item_n):
    return HttpResponse("<body>Подробно элемент</body>")


def catalog_regular(request, regular_n):
    return HttpResponse(regular_n)


def catalog_converter(request, n):
    return HttpResponse(n)
