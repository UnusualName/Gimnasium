import re

import django.core
from django.core.exceptions import ValidationError
import django.db
from django.utils.translation import gettext_lazy as _

from core.models import CatalogAbstraction, CatalogClassificationAbstraction


def validate_perfection(value):
    if not re.search(r"\bпревосходно\b|\bроскошно\b", value.lower()):
        raise ValidationError((f"There is no perfection in {value}"))


class Tag(CatalogClassificationAbstraction):
    class Meta:
        verbose_name = _("Tag")
        verbose_name_plural = _("Tags")


class Category(CatalogClassificationAbstraction):
    weight = django.db.models.IntegerField(
        default=100,
        validators=[
            django.core.validators.MaxValueValidator(32767),
            django.core.validators.MinValueValidator(1),
        ],
        verbose_name=_("Weight"),
    )

    class Meta:
        verbose_name = _("Category")
        verbose_name_plural = _("Categories")


class Item(CatalogAbstraction):
    text = django.db.models.TextField(
        verbose_name=_("Text"),
        help_text=(
            "Должно содержать по крайней мере одно слово "
            "'Превосходно' или 'Роскошно'"
        ),
        validators=[validate_perfection],
    )
    tags = django.db.models.ManyToManyField(Tag)
    category = django.db.models.ForeignKey(
        "category",
        on_delete=django.db.models.CASCADE,
        related_name="item_category",
        help_text="Выберите категорию",
    )

    class Meta:
        verbose_name = _("Item")
        verbose_name_plural = _("Items")
