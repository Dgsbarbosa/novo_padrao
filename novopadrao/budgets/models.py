from django.db import models
from company.models import Clients
# Create your models here.

class Budgets(models.Model):
    
    client = models.ForeignKey(Clients, null=True, on_delete=models.SET_NULL)
    
    number_budgets = models.CharField(max_length=10,unique=True)    
    
    reference = models.CharField(max_length=500, null=True,blank=True)
    
    validity = models.DateField()
    
    term = models.DateField(null=True,blank=True)

    obs = models.TextField(null=True,blank=True)
    
    create_at = models.DateTimeField(auto_now_add=True)
    
    update_at = models.DateTimeField(auto_now=True)
    
    def __str__(self) -> str:
        
        return '{}  {} {}  {} {} '.format(self.client, self.number_budgets, self.reference, self.validity, self.term, self.obs)
    

    
class Services(models.Model):
    
    id_budget = models.ForeignKey(Budgets, default=1, on_delete=models.CASCADE)
    
    descript = models.CharField(max_length=500)
    
    details = models.TextField(null=True,blank=True)
    
    price = models.FloatField(null=True,blank=True)
    
    amount = models.FloatField(null=True,blank=True)
    
    total = models.FloatField(null=True,blank=True)
    
    
    
class Materials(models.Model):
    
    id_budget = models.ForeignKey(Budgets, default=1, on_delete=models.CASCADE)
    
    photo = models.ImageField(upload_to="",blank=True, null=True )
    descript = models.CharField(max_length=500)
    
    details = models.TextField(null=True,blank=True)
    
    price = models.FloatField(null=True,blank=True)
    
    amount = models.FloatField(null=True,blank=True)
    
    total = models.FloatField(null=True,blank=True)

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


