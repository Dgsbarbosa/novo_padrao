from django.contrib.auth.forms import UserCreationForm, UserChangeForm

from .models import CustomUser


class CustomUserCreationForm(UserCreationForm):

    class Meta:
        model = CustomUser
        fields = (
            'first_name',
            'last_name',
            "email",
            "password1", 
            'password2')
        
        
        
        labels = {
            'first_name':('Nome'),            
            'last_name': ('Sobrenome'),
            'password1' : ('Senha')
            }
        
        

       
class CustomUserChangeForm(UserChangeForm):

    class Meta:
        model = CustomUser
        fields = ("email",)