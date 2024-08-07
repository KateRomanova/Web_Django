# Generated by Django 5.0.6 on 2024-06-25 13:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("catalog", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="product",
            name="photo",
            field=models.ImageField(
                blank=True,
                help_text="Загрузите фото продукта",
                null=True,
                upload_to="product/photo",
                verbose_name="Изображение (превью)",
            ),
        ),
        migrations.AlterField(
            model_name="product",
            name="price",
            field=models.IntegerField(
                blank=True,
                help_text="Укажите цену за покупку",
                null=True,
                verbose_name="Цена",
            ),
        ),
    ]
