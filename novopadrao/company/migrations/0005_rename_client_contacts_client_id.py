# Generated by Django 4.2.1 on 2023-05-12 15:39

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("company", "0004_rename_client_address_client_id"),
    ]

    operations = [
        migrations.RenameField(
            model_name="contacts",
            old_name="client",
            new_name="client_id",
        ),
    ]
