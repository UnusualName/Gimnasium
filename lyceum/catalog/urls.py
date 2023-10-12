from django.urls import path, re_path, register_converter

from . import converters, views

register_converter(converters.FourDigitYearConverter, "n_converter")

urlpatterns = [
    path("", views.item_list),
    path("<int:item_n>/", views.item_detail),
    re_path(r"^re/(?P<regular_n>[+]?\d+)/$", views.catalog_regular),
    path("converter/<n_converter:n>/", views.catalog_converter),
]
