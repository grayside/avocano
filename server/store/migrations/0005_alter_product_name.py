# Generated by Django 4.2 on 2023-04-13 04:19

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("store", "0004_alter_siteconfig_base_font_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="product",
            name="name",
            field=models.CharField(max_length=64, unique=True),
        ),
    ]
