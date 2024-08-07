# Generated by Django 4.2.2 on 2024-07-17 12:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("catalog", "0006_product_owner"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="product",
            options={
                "ordering": ["name", "category"],
                "permissions": [
                    ("can_edit_product_description", "Can edit product description"),
                    ("can_edit_product_category", "Can edit product category"),
                    ("can_cancel_publication", "Can cancel publication of product"),
                ],
                "verbose_name": "Продукт",
                "verbose_name_plural": "Продукты",
            },
        ),
        migrations.AddField(
            model_name="product",
            name="is_published",
            field=models.BooleanField(
                default=False,
                help_text="Опубликовать запись",
                verbose_name="Опубликовано",
            ),
        ),
    ]
