import django.db


class CatalogAbstraction(django.db.models.Model):
    id = django.db.models.BigAutoField(primary_key=True, verbose_name="id")
    is_published = django.db.models.BooleanField(
        default=True, verbose_name=("опубликовано")
    )
    name = django.db.models.CharField(
        verbose_name=("название"),
        max_length=150,
        help_text="Максимум 150 символов",
    )

    class Meta:
        abstract = True

    def __str__(self):
        return self.name[:15]


class CatalogClassificationAbstraction(CatalogAbstraction):
    slug = django.db.models.TextField(
        unique=True,
        verbose_name=("слаг"),
        validators=[
            django.core.validators.MaxLengthValidator(200),
            django.core.validators.RegexValidator(regex=r"[-a-zA-Z\d_]+"),
        ],
    )

    class Meta:
        abstract = True
