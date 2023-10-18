from core.models import CatalogAbstraction, CatalogClassificationAbstraction
import django.core
from django.core.exceptions import ValidationError
import django.db


def validate_perfection(value):
    if not ("превосходно" in value.lower() or "роскошно" in value.lower()):
        raise ValidationError((f"There is no perfection in {value}"))


class Tag(CatalogClassificationAbstraction):
    class Meta:
        verbose_name = "Тег"
        verbose_name_plural = "Теги"


class Category(CatalogClassificationAbstraction):
    weight = django.db.models.IntegerField(
        default=100,
        validators=[
            django.core.validators.MaxValueValidator(32767),
            django.core.validators.MinValueValidator(0),
        ],
        verbose_name="Вес",
    )

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"


class Item(CatalogAbstraction):
    text = django.db.models.TextField(
        verbose_name="Текст",
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
        verbose_name = "Товар"
        verbose_name_plural = "Товары"
