# Generated by Django 5.1.2 on 2024-10-31 22:22

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("store", "0011_alter_product_details"),
    ]

    operations = [
        migrations.AddField(
            model_name="customer",
            name="wishlist",
            field=models.JSONField(blank=True, default=dict, null=True),
        ),
    ]
