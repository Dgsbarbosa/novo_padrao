# Generated by Django 4.2.1 on 2023-06-10 00:24

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("budgets", "0011_alter_payments_discount"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="budgets",
            name="condition",
        ),
        migrations.AddField(
            model_name="budgets",
            name="situation",
            field=models.CharField(
                blank=True,
                choices=[
                    ("Pendente", "Pendente"),
                    ("Aprovado", "Aprovado"),
                    ("Cancelado", "Cancelado"),
                    ("Em andamento", "Em andamento"),
                    ("Concluido", "Concluido"),
                ],
                default="Pendente",
                max_length=500,
                null=True,
            ),
        ),
    ]