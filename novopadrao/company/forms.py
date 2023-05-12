
from django import forms

from .models import Clients, Contacts, Address


class ClientForm(forms.ModelForm):
    class Meta:
        model = Clients
        fields = ('name', 'client_type',)
        labels = {'name': ('Nome'), 'client_type': ('Tipo de cliente')}


class AddressForm(forms.ModelForm):
    class Meta:
        model = Address
        fields = ('street',
                  'bairro',
                  'city',
                  'state',
                  )
        labels = {'street':('Rua'),
                  'city': ('Cidade'),
                  'state' : ('Estado'),}


class ContactsForm(forms.ModelForm):
    class Meta:
        model = Contacts
        fields = ('telefone1',
                  'telefone2',
                  'email',)
        labels = {}
        
        widgets = {
            "email" : forms.TextInput(attrs={'class':'form-control', 'placeholder':"Digite seu email"}),
        }
