# Generated by Django 5.1.2 on 2024-10-31 18:43

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("store", "0010_product_details_delete_wishlist"),
    ]

    operations = [
        migrations.AlterField(
            model_name="product",
            name="details",
            field=models.TextField(blank=True, default=""),
        ),
    ]
