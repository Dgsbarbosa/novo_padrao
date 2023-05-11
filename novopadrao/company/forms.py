
from django import forms

from .models import Clients, Contacts, Address

class ClientForm(forms.ModelForm):
    class Meta:
        model = Clients
        fields = '__all__'
        labels = {'name': ('Nome'), 'client_type':('Tipo de cliente')}
        
        

        
    
