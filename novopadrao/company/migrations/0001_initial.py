# Generated by Django 4.2.1 on 2023-06-27 19:03

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="Clients",
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
                ("name", models.CharField(max_length=255)),
                (
                    "client_type",
                    models.CharField(
                        blank=True,
                        choices=[("1", "Pessoa Fisica"), ("2", "Pessoa Juridica")],
                        max_length=25,
                        null=True,
                    ),
                ),
                ("create_at", models.DateTimeField(auto_now_add=True)),
                ("update_at", models.DateTimeField(auto_now=True)),
                (
                    "user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Contacts",
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
                    "telefone1",
                    models.CharField(blank=True, max_length=30, null=True, unique=True),
                ),
                (
                    "telefone2",
                    models.CharField(blank=True, max_length=30, null=True, unique=True),
                ),
                (
                    "email",
                    models.EmailField(
                        blank=True, max_length=255, null=True, unique=True
                    ),
                ),
                (
                    "client_id",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="company.clients",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Address",
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
                ("street", models.CharField(blank=True, max_length=255, null=True)),
                ("bairro", models.CharField(blank=True, max_length=255, null=True)),
                ("city", models.CharField(blank=True, max_length=255, null=True)),
                ("cep", models.CharField(blank=True, max_length=255, null=True)),
                (
                    "state",
                    models.CharField(
                        blank=True,
                        choices=[
                            ("AC", "Acre"),
                            ("AL", "Alagoas"),
                            ("AP", "Amapa"),
                            ("AM", "Amazonas"),
                            ("BA", "Bahia"),
                            ("CE", "Ceara"),
                            ("DF", "Distrito Federal"),
                            ("ES", "Espirito Santo"),
                            ("GO", "Goias"),
                            ("MA", "Maranhao"),
                            ("MT", "Mato Grosso"),
                            ("MS", "Mato Grosso do Sul"),
                            ("MG", "Minas Gerais"),
                            ("PA", "Para"),
                            ("PB", "Paraiba"),
                            ("PR", "Parana"),
                            ("PE", "Pernambuco"),
                            ("PI", "Piaui"),
                            ("RJ", "Rio de Janeiro"),
                            ("RN", "Rio Grande do Norte"),
                            ("RS", "Rio Grande do Sul"),
                            ("RO", "Rondonia"),
                            ("RR", "Roraima"),
                            ("SC", "Santa Catarina"),
                            ("SP", "Sao Paulo"),
                            ("SE", "Sergipe"),
                            ("TO", "Tocantins"),
                        ],
                        max_length=25,
                        null=True,
                    ),
                ),
                (
                    "client_id",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="company.clients",
                    ),
                ),
            ],
        ),
    ]
