

from typing import Any
from django.db import models
from company.models import Clients
from django.contrib.auth import get_user_model
from company.models import Clients

# Create your models here.


class Budgets(models.Model):

    SITUATION = ("Pendente", "Pendente"), ("Aprovado", "Aprovado"), ("Cancelado",
                                                                     "Cancelado"), ("Em andamento", "Em andamento"), ("Concluido", "Concluido")

    client = models.ForeignKey(Clients,  null=True, on_delete=models.SET_NULL)

    user = models.ForeignKey(
        get_user_model(),  null=True, on_delete=models.CASCADE)

    number_budgets = models.CharField(max_length=10, unique=True)

    reference = models.CharField(max_length=500, null=True, blank=True)

    situation = models.CharField(
        max_length=500,
        choices=SITUATION,
        null=True,
        blank=True,
        default="Pendente"
    )
    validity = models.DateField(null=True, blank=True)

    term = models.CharField(max_length=100, null=True, blank=True)

    obs = models.TextField(null=True, blank=True)

    create_at = models.DateTimeField(auto_now_add=True)

    update_at = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:

        return '{} {} {} {}  {} {} {}'.format(self.number_budgets, self.client, self.situation, self.reference, self.validity, self.term, self.obs)


class Services(models.Model):

    id_budget = models.ForeignKey(Budgets, default=1, on_delete=models.CASCADE)

    descript = models.CharField(max_length=500)

    details = models.TextField(null=True, blank=True)

    price = models.TextField(null=True, blank=True)

    amount = models.TextField(null=True, blank=True)

    total = models.TextField(null=True, blank=True)

    def __str__(self) -> str:

        return '{} - {} - {} - {} - {} - {}'.format(self.id_budget.id, self.descript, self.details, self.price, self.amount, self.total)


class Materials(models.Model):

    id_budget = models.ForeignKey(Budgets,  on_delete=models.CASCADE)

    descript = models.CharField(max_length=500, null=True, blank=True)

    details = models.TextField(null=True, blank=True)

    price = models.TextField(null=True, blank=True)

    amount = models.TextField(null=True, blank=True)

    total = models.TextField(null=True, blank=True)

    def __str__(self) -> str:
        return '{} - {} - {} - {} - {} - {}'.format(self.id_budget.id, self.descript, self.details, self.price, self.amount, self.total)


class Payments(models.Model):

    METHODS = [
        ("dinheiro", "Dinheiro"), 
        ("pix", "Pix"),        
        ("tranferencia", "Tranferencia"),
        ("credito", "Cartao de Credito"),    
        ("debito", "Cartao de Debito"),
    ]

    DISCOUNT = (('none', 'Sem desconto'), ('valor', 'Valor'),
                ('porcentagem', 'Porcentagem'))

    CONDITION = (("a vista", "a vista"), ("sinal", "sinal"),
                 ("parcelas", "parcelas"))

    id_budget = models.ForeignKey(Budgets,  on_delete=models.CASCADE)

    discount = models.CharField(
        max_length=500,
        choices=DISCOUNT,
        null=True,
        blank=True,
    )

    condition = models.CharField(
        max_length=500,
        choices=CONDITION,
        null=True,
        blank=True,
    )

    methods = models.CharField(
        max_length=500,
        choices=METHODS,
        null=True,
        blank=True,
    )

    obs = models.TextField(
        max_length=500,
        null=True,
        blank=True,
    )

    def __str__(self) -> str:
        return '{} - {} - {} - {} - {}'.format(self.id_budget.id, self.discount, self.condition, self.methods, self.obs)


class Totals(models.Model):

    id_budget = models.ForeignKey(Budgets,  on_delete=models.CASCADE)

    total_services = models.CharField(
        max_length=500,
        null=True,
        blank=True
    )

    total_materials = models.CharField(
        max_length=500,
        null=True,
        blank=True
    )

    discount = models.CharField(
        max_length=500,
        null=True,
        blank=True
    )

    parcels = models.CharField(
        max_length=500,
        null=True,
        blank=True
    )

    total_final = models.CharField(
        max_length=500,
        null=True,
        blank=True
    )

    def __str__(self) -> str:
        return '{} - {} - {} - {} - {} - {}'.format(self.id_budget.id, self.total_services, self.total_materials, self.discount, self.parcels, self.total_final)
