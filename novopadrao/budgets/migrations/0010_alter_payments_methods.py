# Generated by Django 4.2.1 on 2023-06-09 23:31

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("budgets", "0009_alter_payments_condition_alter_payments_discount_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="payments",
            name="methods",
            field=models.CharField(
                blank=True,
                choices=[
                    ("dinheiro", "Dinheiro"),
                    ("pix", "Pix"),
                    ("tranferencia", "Tranferencia"),
                    ("credito", "Cartao de Credito"),
                    ("debito", "Cartao de Debito"),
                ],
                max_length=50,
                null=True,
            ),
        ),
    ]
