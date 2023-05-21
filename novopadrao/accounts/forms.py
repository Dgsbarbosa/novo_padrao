

from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.forms import PasswordInput

from .models import CustomUser, EditPerfilCompany, PerfilCompany


class CustomUserCreationForm(UserCreationForm):
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['password1'].label = 'Senha'
        self.fields['password2'].label = 'Confirme a senha'
        self.fields['password1'].help_text = ""        
        self.fields['password2'].help_text = 'Digite a mesma senha de antes.'

    class Meta:
        model = CustomUser
        fields = (
            'first_name',
            'last_name',
            'email',
            'username'
            
             
        )
      
        
        labels = {
            'first_name':('Nome'),            
            'last_name': ('Sobrenome'),
            'username': ('Nome de usuario')
            }
       

       
class CustomUserChangeForm(UserCreationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
        self.fields['password'].label = 'Senha'
     
    class Meta:
        model = CustomUser
        fields = ("email",)
        
        
class CustomUserEditForm(UserCreationForm):
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['password1'].label = 'Senha'
        self.fields['password1'].help_text = ''        
        self.fields['password2'].label = 'Confirme a senha'
        self.fields['password2'].help_text = 'Entre com a mesma senha'     
 
    class Meta:
    
        model = CustomUser
        fields = (
            'first_name',
            'last_name',
            'email',
            'username'
        )
               
        
           
        labels = {
            'first_name':('Nome'),            
            'last_name': ('Sobrenome'),
            'username': ('Nome de usuario')
            }


class CustomPerfilCompanyForm(forms.ModelForm):
    class Meta:
        model = PerfilCompany
        
        fields = (
            'logo',
            'name',            
            'razaoSocial',
            'cnpj',
            'email',
            'phone1',
            'phone2',
            'email'

            
        )
        
        labels={
            'logo':('Logotipo'),
            'name':('Nome da Empresa'),            
            'razaoSocial':('Razao Social'),
            'phone1' : ('Telefone'),
            'phone2' : ('Telefone 2'),
            
            
        }
    
class EditPerfilCompanyForm(forms.ModelForm):
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        #self.fields['currently'].label = 'Senha'
        # self.fields['password1'].help_text = ''        
        # self.fields['password2'].label = 'Confirme a senha'
        # self.fields['password2'].help_text = 'Entre com a mesma senha'     
 
    class Meta:
    
        model = PerfilCompany
        
        fields = (
            'logo',
            'name',            
            'razaoSocial',
            'cnpj',
            'email',
            'phone1',
            'phone2', 
            
            
        )
        
        labels={
            'logo': ('Logotipo'),
            'name':('Nome da Empresa'),            
            'razaoSocial':('Razao Social'),
             'phone1' : ('Telefone'),
            'phone2' : ('Telefone 2')
            
        } 
        
 

