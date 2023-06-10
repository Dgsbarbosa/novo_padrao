# Generated by Django 4.2.1 on 2023-06-10 16:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("budgets", "0012_remove_budgets_condition_budgets_situation"),
    ]

    operations = [
        migrations.AlterField(
            model_name="materials",
            name="id_budget",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to="budgets.budgets"
            ),
        ),
        migrations.AlterField(
            model_name="payments",
            name="id_budget",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to="budgets.budgets"
            ),
        ),
        migrations.CreateModel(
            name="Totals",
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
                (
                    "total_services",
                    models.CharField(blank=True, max_length=500, null=True),
                ),
                (
                    "total_materials",
                    models.CharField(blank=True, max_length=500, null=True),
                ),
                ("discount", models.CharField(blank=True, max_length=500, null=True)),
                ("parcels", models.CharField(blank=True, max_length=500, null=True)),
                (
                    "total_final",
                    models.CharField(blank=True, max_length=500, null=True),
                ),
                (
                    "id_budget",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="budgets.budgets",
                    ),
                ),
            ],
        ),
    ]
