# Generated by Django 4.2.1 on 2023-05-21 15:51

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("accounts", "0003_perfilcompany_email"),
    ]

    operations = [
        migrations.AlterField(
            model_name="perfilcompany",
            name="email",
            field=models.EmailField(
                blank=True, max_length=254, null=True, unique=True, verbose_name="email"
            ),
        ),
    ]
