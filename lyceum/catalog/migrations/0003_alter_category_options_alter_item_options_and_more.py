# Generated by Django 4.2.5 on 2023-10-19 20:18

import catalog.models
import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("catalog", "0002_alter_item_text"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="category",
            options={
                "verbose_name": "category",
                "verbose_name_plural": "categories",
            },
        ),
        migrations.AlterModelOptions(
            name="item",
            options={"verbose_name": "item", "verbose_name_plural": "items"},
        ),
        migrations.AlterModelOptions(
            name="tag",
            options={"verbose_name": "tag", "verbose_name_plural": "tags"},
        ),
        migrations.AlterField(
            model_name="category",
            name="is_published",
            field=models.BooleanField(
                default=True, verbose_name="is_published"
            ),
        ),
        migrations.AlterField(
            model_name="category",
            name="name",
            field=models.CharField(
                help_text="Максимум 150 символов",
                max_length=150,
                verbose_name="name",
            ),
        ),
        migrations.AlterField(
            model_name="category",
            name="slug",
            field=models.TextField(
                unique=True,
                validators=[
                    django.core.validators.MaxLengthValidator(200),
                    django.core.validators.RegexValidator(
                        regex="[-a-zA-Z\\d_]+"
                    ),
                ],
                verbose_name="slag",
            ),
        ),
        migrations.AlterField(
            model_name="category",
            name="weight",
            field=models.IntegerField(
                default=100,
                validators=[
                    django.core.validators.MaxValueValidator(32767),
                    django.core.validators.MinValueValidator(1),
                ],
                verbose_name="weight",
            ),
        ),
        migrations.AlterField(
            model_name="item",
            name="is_published",
            field=models.BooleanField(
                default=True, verbose_name="is_published"
            ),
        ),
        migrations.AlterField(
            model_name="item",
            name="name",
            field=models.CharField(
                help_text="Максимум 150 символов",
                max_length=150,
                verbose_name="name",
            ),
        ),
        migrations.AlterField(
            model_name="item",
            name="text",
            field=models.TextField(
                help_text="Должно содержать по крайней мере одно слово 'Превосходно' или 'Роскошно'",
                validators=[catalog.models.validate_perfection],
                verbose_name="text",
            ),
        ),
        migrations.AlterField(
            model_name="tag",
            name="is_published",
            field=models.BooleanField(
                default=True, verbose_name="is_published"
            ),
        ),
        migrations.AlterField(
            model_name="tag",
            name="name",
            field=models.CharField(
                help_text="Максимум 150 символов",
                max_length=150,
                verbose_name="name",
            ),
        ),
        migrations.AlterField(
            model_name="tag",
            name="slug",
            field=models.TextField(
                unique=True,
                validators=[
                    django.core.validators.MaxLengthValidator(200),
                    django.core.validators.RegexValidator(
                        regex="[-a-zA-Z\\d_]+"
                    ),
                ],
                verbose_name="slag",
            ),
        ),
    ]
