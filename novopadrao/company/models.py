from django.db import models
from django.contrib.auth import get_user_model

# Create your models here.
class Clients(models.Model):
    TIPOS = ("1","Pessoa Fisica"),("2","Pessoa Juridica")
    
    nome = models.CharField(max_length=255, )
    
    endereco = models.CharField(max_length=255)
    
    tipo = models.CharField(
        max_length=10,
        choices=TIPOS,
        null=True, 
        blank=True
        )
    
    telefone1 = models.CharField(max_length=255)
    
    telefone2 = models.CharField(max_length=255,null=True, blank=True)

    bairro = models.CharField(max_length=255,null=True, blank=True)

    cidade = models.CharField(max_length=255,null=True, blank=True)

    estado = models.CharField(max_length=255,null=True, blank=True)
    
    email = models.CharField(max_length=255,null=True, blank=True)
    
    create_at = models.DateTimeField(auto_now_add=True)

    update_at = models.DateTimeField(auto_now=True)
    
    def __str__(self) -> str:
        return self.nome
    

    