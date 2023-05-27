from django import forms
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.db import models
from django.utils import timezone
from django.utils.translation import gettext_lazy as _
from django.contrib.auth import get_user_model
from .manage import CustomUserManager
from django.contrib.auth.password_validation import validate_password
from django.core.exceptions import ValidationError


class CustomUser(AbstractBaseUser, PermissionsMixin):
    
    first_name = models.CharField(_('Nome'),max_length=100, )
    
    last_name = models.CharField(max_length=100)
    
    email = models.EmailField(_("email"), unique=True, )  
      
    username = models.CharField(max_length=100,unique=False, blank=True, null=True,)
    
    is_staff = models.BooleanField(default=False)
    
    is_active = models.BooleanField(default=True)
    
    date_joined = models.DateTimeField(default=timezone.now)

    
    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    objects = CustomUserManager()
    
    
    
    class Meta:
        verbose_name = _('user')
        verbose_name_plural = _('users')    
    
        def __str__(self):
            
            return self.id, self.email    
        
        

class UpdateUser(forms.ModelForm):
    
    first_name = models.CharField(_('Nome'),max_length=100, )
    
    last_name = models.CharField(max_length=100)
    
    email = models.EmailField(_("email"), unique=True,   )  
      
    username = models.CharField(max_length=100,unique=False, blank=True, null=True,)

    class Meta:
        model = CustomUser
        fields = ['first_name','last_name','username', 'email']
        
class PerfilCompany(models.Model) :
    
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    
    name = models.CharField(max_length=255, help_text="Campo Obrigatorio " )
    
    logo = models.ImageField(upload_to="",blank=True, null=True )
    
    
    razaoSocial = models.CharField(max_length=255, blank=True, null=True )
    
    cnpj = models.CharField(max_length=255, blank=True, null=True )
    
    phone1 = models.CharField(max_length=255, blank=True, null=True )
    
    phone2 = models.CharField(max_length=255, blank=True, null=True )
    
    email = models.EmailField(_("email"), unique=True, blank=True, null=True )
    USERNAME_FIELD = "name"
    REQUIRED_FIELDS = []
    
    
    def __str__(self) -> str:
        return '{} - {} - {} - {} ' .format( self.name,self.logo,self.razaoSocial,  self.cnpj)

    
class EditPerfilCompany(models.Model) :
    
    logo = models.ImageField(upload_to="",blank=True, null=True )
    name = models.CharField(max_length=255, help_text="Campo Obrigatorio " )   
    
    
    razaoSocial = models.CharField(max_length=255, blank=True, null=True )
    
    cnpj = models.CharField(max_length=255, blank=True, null=True )
    
    phone1 = models.CharField(max_length=255, blank=True, null=True )
    
    phone2 = models.CharField(max_length=255, blank=True, null=True )
    
    email = models.EmailField(_("email"), unique=True)
   
 

    
    