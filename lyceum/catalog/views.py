from django.http import HttpResponse


def item_list(request):
    return HttpResponse("<body>Список элементов</body>")


def item_detail(request, item_n):
    return HttpResponse("<body>Подробно элемент</body>")


def catalog_n(request, n):
    return HttpResponse(n)
