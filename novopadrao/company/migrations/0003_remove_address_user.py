# Generated by Django 4.2.1 on 2023-05-24 16:33

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("company", "0002_delete_budget_delete_materials_delete_services"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="address",
            name="user",
        ),
    ]
