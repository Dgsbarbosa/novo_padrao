from django import forms
from .models import Clients

class ClientForm(forms.ModelForm):
    class Meta:
        model = Clients
        fields = ('nome','tipo', 'endereco', 'telefone1', 'telefone2', 'email', 'bairro','cidade', 'estado')