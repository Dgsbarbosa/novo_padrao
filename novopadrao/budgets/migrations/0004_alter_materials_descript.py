# Generated by Django 4.2.1 on 2023-06-30 20:20

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("budgets", "0003_alter_payments_condition_alter_payments_methods"),
    ]

    operations = [
        migrations.AlterField(
            model_name="materials",
            name="descript",
            field=models.CharField(blank=True, default="", max_length=500, null=True),
        ),
    ]