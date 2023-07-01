# Generated by Django 4.2.1 on 2023-06-30 19:38

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("budgets", "0002_alter_payments_condition"),
    ]

    operations = [
        migrations.AlterField(
            model_name="payments",
            name="condition",
            field=models.CharField(
                blank=True,
                choices=[
                    ("a vista", "a vista"),
                    ("sinal", "sinal"),
                    ("parcelas", "parcelas"),
                ],
                max_length=500,
                null=True,
            ),
        ),
        migrations.AlterField(
            model_name="payments",
            name="methods",
            field=models.CharField(blank=True, max_length=500, null=True),
        ),
    ]
