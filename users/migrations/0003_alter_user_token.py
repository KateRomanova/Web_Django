# Generated by Django 4.2.2 on 2024-07-12 15:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("users", "0002_user_token"),
    ]

    operations = [
        migrations.AlterField(
            model_name="user",
            name="token",
            field=models.CharField(
                blank=True, max_length=100, null=True, verbose_name="token"
            ),
        ),
    ]
