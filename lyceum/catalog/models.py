import re

import django.core
from django.core.exceptions import ValidationError
import django.db

from core.models import CatalogAbstraction, CatalogClassificationAbstraction


def validate_perfection(value):
    if not re.search(r"\bпревосходно\b|\bроскошно\b", value.lower()):
        raise ValidationError((f"There is no perfection in {value}"))


class Tag(CatalogClassificationAbstraction):
    class Meta:
        verbose_name = "тег"
        verbose_name_plural = "теги"


class Category(CatalogClassificationAbstraction):
    weight = django.db.models.IntegerField(
        default=100,
        validators=[
            django.core.validators.MaxValueValidator(32767),
            django.core.validators.MinValueValidator(1),
        ],
        verbose_name=("вес"),
    )

    class Meta:
        verbose_name = "категория"
        verbose_name_plural = "категории"


class Item(CatalogAbstraction):
    text = django.db.models.TextField(
        verbose_name=("текст"),
        help_text=(
            "Должно содержать по крайней мере одно слово "
            "'Превосходно' или 'Роскошно'"
        ),
        validators=[validate_perfection],
    )
    tags = django.db.models.ManyToManyField(Tag, verbose_name=("tags"))
    category = django.db.models.ForeignKey(
        "category",
        on_delete=django.db.models.CASCADE,
        related_name="item_category",
        help_text="Выберите категорию",
        verbose_name=("категория"),
    )

    class Meta:
        verbose_name = "товар"
        verbose_name_plural = "товары"
