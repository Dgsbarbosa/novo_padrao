

from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.forms import PasswordInput

from .models import CustomUser


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
            
             
        )
      
        
        labels = {
            'first_name':('Nome'),            
            'last_name': ('Sobrenome'),
            
            }
       

       
class CustomUserChangeForm(UserChangeForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
        self.fields['password'].label = 'Senha'
       

        
        
    class Meta:
        model = CustomUser
        fields = ("email",)