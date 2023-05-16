from django import forms
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.db import models
from django.utils import timezone
from django.utils.translation import gettext_lazy as _

from .manage import CustomUserManager


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
            
            return self.email

class UpdateUserForm(forms.ModelForm):
    
    first_name = models.CharField(_('Nome'),max_length=100, )
    
    last_name = models.CharField(max_length=100)
    
    email = models.EmailField(_("email"), unique=True,   )  
      
    username = models.CharField(max_length=100,unique=False, blank=True, null=True,)

    class Meta:
        model = CustomUser
        fields = ['first_name','last_name','username', 'email']