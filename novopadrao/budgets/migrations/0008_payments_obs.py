# Generated by Django 4.2.1 on 2023-06-09 17:52

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("budgets", "0007_remove_materials_photo_alter_materials_descript"),
    ]

    operations = [
        migrations.AddField(
            model_name="payments",
            name="obs",
            field=models.TextField(default="", max_length=500),
            preserve_default=False,
        ),
    ]
