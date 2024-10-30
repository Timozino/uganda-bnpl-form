# Generated by Django 5.1.1 on 2024-10-30 07:45

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        ("Bio_Data", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="StoreDetail",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("sales_agent_name", models.CharField(max_length=100)),
                (
                    "product_usage",
                    models.CharField(
                        choices=[("C", "Commercial"), ("D", "Domestic")], max_length=1
                    ),
                ),
                ("store_name", models.CharField(max_length=255)),
                ("product_brand", models.CharField(max_length=100)),
                ("freezer_size", models.CharField(max_length=100)),
                ("reference_kb_number", models.CharField(max_length=50)),
                ("category", models.CharField(max_length=255)),
                ("selling_for", models.CharField(max_length=255)),
                (
                    "bio_data",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="store_details",
                        to="Bio_Data.biodata",
                    ),
                ),
            ],
        ),
    ]
