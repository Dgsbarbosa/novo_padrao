from django.db import models

from django.contrib.auth.models import User
from django.contrib.auth import get_user_model
from phonenumber_field.modelfields import PhoneNumberField


# Create your models here.

CLIENT_TYPE = [
    ("1","Pessoa Fisica"),
    ("2","Pessoa Juridica")
    ]


STATES = [
    ('AC', 'Acre'),
    ('AL', 'Alagoas'),
    ('AP', 'Amapa'),
    ('AM', 'Amazonas'),
    ('BA', 'Bahia'),
    ('CE', 'Ceara'),
    ('DF', 'Distrito Federal'),
    ('ES', 'Espirito Santo'),
    ('GO', 'Goias'),
    ('MA', 'Maranhao'),
    ('MT', 'Mato Grosso'),
    ('MS', 'Mato Grosso do Sul'),
    ('MG', 'Minas Gerais'),
    ('PA', 'Para'),
    ('PB', 'Paraiba'),
    ('PR', 'Parana'),
    ('PE', 'Pernambuco'),
    ('PI', 'Piaui'),
    ('RJ', 'Rio de Janeiro'),
    ('RN', 'Rio Grande do Norte'),
    ('RS', 'Rio Grande do Sul'),
    ('RO', 'Rondonia'),
    ('RR', 'Roraima'),
    ('SC', 'Santa Catarina'),
    ('SP', 'Sao Paulo'),
    ('SE', 'Sergipe'),
    ('TO', 'Tocantins')
]


class Clients(models.Model): 
    
    
    name = models.CharField(max_length=255)
    
    client_type = models.CharField(
        max_length=25,
        choices=CLIENT_TYPE,
        null=True, 
        blank=True,
        )
    
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)    
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)
    
    def __str__(self) -> str:
        return '{} - {} ' .format( self.name, self.client_type)

    
class Address(models.Model):
    
    
    client_id =  models.ForeignKey(Clients, on_delete=models.CASCADE)
    
    street = models.CharField(max_length=255, null=True, blank=True)
    
    bairro = models.CharField(max_length=255,null=True, blank=True)
    
    city = models.CharField(max_length=255,null=True, blank=True)
    
    state = models.CharField(
        max_length=25,
        choices=STATES,
        null=True, 
        blank=True,
        )
    
    def __str__(self) -> str:
        return '{} - {} - {} - {}' .format( self.street, self.bairro, self.city, self.state)


class Contacts(models.Model):
    
    
    client_id =  models.ForeignKey(Clients, on_delete=models.CASCADE)
    
    telefone1 = models.CharField(max_length=15, unique=True, null=False, blank=False, ) 
       
    telefone2 = models.CharField(max_length=15, unique=True, null=False, blank=False, ) 
    
    email = models.EmailField(max_length=255, unique=True,  null=True, blank=True)
    
    def __str__(self) -> str:
        
        return '{} {} {}'.format( self.telefone1 , self.telefone2 , self.email) 
    



    

    
    
class Budget(models.Model):
    
    ...
    
class Services(models.Model):
    ...
    
class Materials(models.Model):
    ...

class PayMethods():
    
    METHODS = ("1","Dinheiro"),("2","Pix"),("3","Tranferencia"), ("4","Carta de Credito"),("5","Cartao de Debito")
    
    methods = models.CharField(
        max_length=50,
        choices=METHODS,
        null=True, 
        blank=True,
        )


    