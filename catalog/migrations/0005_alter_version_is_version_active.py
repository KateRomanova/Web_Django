# Generated by Django 5.0.6 on 2024-07-04 12:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("catalog", "0004_alter_version_is_version_active"),
    ]

    operations = [
        migrations.AlterField(
            model_name="version",
            name="is_version_active",
            field=models.BooleanField(
                default=False,
                help_text="является ли версия активной",
                verbose_name="Активная версия",
            ),
        ),
    ]
