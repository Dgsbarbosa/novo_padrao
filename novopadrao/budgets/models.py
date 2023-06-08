

from typing import Any
from django.db import models
from company.models import Clients
from django.contrib.auth import get_user_model
from company.models import Clients

# Create your models here.

class Budgets(models.Model):
    
    CONDITION = ("Pendente","Pendente"),("Aprovado","Aprovado"),("Cancelado","Cancelado"),("Em andamento","Em andamento"),("Concluido","Concluido")
   
    client = models.ForeignKey(Clients,  null=True, on_delete=models.SET_NULL)
     
    user = models.ForeignKey(get_user_model(),  null=True, on_delete=models.CASCADE)
     
    number_budgets = models.CharField(max_length=10,unique=True)   
    
    reference = models.CharField(max_length=500, null=True,blank=True)
    
    condition = models.CharField(
        max_length=500,
        choices=CONDITION,
        null=True, 
        blank=True,
        default="1"
    )
    validity = models.DateField(null=True,blank=True)
    
    term = models.CharField(max_length=100,null=True,blank=True)

    obs = models.TextField(null=True,blank=True)
    
    create_at = models.DateTimeField(auto_now_add=True)
    
    update_at = models.DateTimeField(auto_now=True)
    
    
    
    def __str__(self) -> str:
        
        return '{} {} {} {}  {} {} {}'.format(self.number_budgets,self.client,self.condition, self.reference, self.validity, self.term, self.obs)
    
    
    
class Services(models.Model):
    
    id_budget = models.ForeignKey(Budgets, default=1, on_delete=models.CASCADE)
    
    descript = models.CharField(max_length=500)
    
    details = models.TextField(null=True,blank=True)
    
    price = models.TextField(null=True,blank=True)
    
    amount = models.TextField(null=True,blank=True)
    
    total = models.TextField(null=True,blank=True)
    def __str__(self) -> str:
        
        return '{} {} {} {} {}'.format(self.descript,self.details, self.price, self.amount, self.total)
    
    
class Materials(models.Model):
    
    id_budget = models.ForeignKey(Budgets, default=1, on_delete=models.CASCADE)
    
    descript = models.CharField(max_length=500, null=True,blank=True)
    
    details = models.TextField(null=True,blank=True)
    
    price = models.TextField(null=True,blank=True)
    
    amount = models.TextField(null=True,blank=True)
    
    total = models.TextField(null=True,blank=True)
    
    def __str__(self) -> str:
        return '{} - {} - {} - {} - {}'.format(self.descript, self.details, self.price, self.amount, self.total)

class Payments(models.Model):
    
    METHODS = ("1","Dinheiro"),("2","Pix"),("3","Tranferencia"), ("4","Cartao de Credito"),("5","Cartao de Debito")
    
    DISCOUNT = ('1','Valor'),('2','Porcentagem')
    
    CONDITION = ("1","a vista"), ("2","sinal"), ("3","parcelas")
    
    
    id_budget = models.ForeignKey(Budgets, default=1, on_delete=models.CASCADE)
    
    
    discount = models.CharField(
        max_length=500,
        choices=DISCOUNT,
        null=True, 
        blank=True,
        )
    
    
    condition = models.CharField(
        max_length=50,
        choices=CONDITION,
        null=True, 
        blank=True,
        )
    
    
    methods = models.CharField(
        max_length=50,
        choices=METHODS,
        null=True, 
        blank=True,
        )


