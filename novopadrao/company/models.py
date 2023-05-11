from django.db import models
from django.forms import ModelForm
from django.contrib.auth import get_user_model


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

    
class Address(models.Model):
    
    
    
    rua = models.CharField(max_length=255)
    
    bairro = models.CharField(max_length=255,null=True, blank=True)
    
    cidade = models.CharField(max_length=255,null=True, blank=True)
    
    estado = models.CharField(
        max_length=25,
        choices=STATES,
        null=True, 
        blank=True,
        )
    
    def __str__(self) -> str:
        return '{} - {} - {} - {}' .format( self.rua, self.bairro, self.cidade, self.estado)


class Contacts(models.Model):
    
    

    
    telefone1 = models.CharField(max_length=15, unique=True) 
       
    telefone2 = models.CharField(max_length=255,null=True, blank=True)
    
    email = models.EmailField(max_length=255)
    
    def __str__(self) -> str:
        return self.telefone1, self.telefone2, self.email 
    
class Clients(models.Model): 
    
    
    name = models.CharField(max_length=255)
    
    client_type = models.CharField(
        max_length=25,
        choices=CLIENT_TYPE,
        null=True, 
        blank=True,
        )
    
    endereco = models.ManyToManyField(Address)
    
    contacts = models.ManyToManyField(Contacts)
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)    
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)
    
    def __str__(self) -> str:
        return self.name



    

    
    
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


    