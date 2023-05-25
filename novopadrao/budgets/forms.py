
from typing import Any, Dict, Mapping, Optional, Type, Union
from django import forms
from django.core.files.base import File
from django.db.models.base import Model
from django.forms.utils import ErrorList

from .models import Budgets,Services, Materials,Payments 


class BudgetsForm(forms.ModelForm):
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
        
        
          
        for i in  self.fields:
            
            self.fields[i].error_messages = {'required': 'Campo obrigatorio'}
        
            self.fields[i].required = False
  
        
    class Meta:
        model = Budgets
        fields = [
            'number_budgets', 
            'client',
            'reference',
            'validity',
            'term',
            'obs',
            
            ]
        labels = {
            'client':('Cliente'),
            'number_budgets':('Numero do Pedido'),
            'reference':('Referencia'),
            'validity': ('Validade'),
            'term': ('Prazo de execucao'),
            'obs':('Observacao')
        }
        widgets = {
            
            
            "obs": forms.Textarea(
                attrs={"cols": 80, "rows": 5}),
        }
        
        
class ServicesForm(forms.ModelForm):
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
       
        for i in  self.fields:
            
            self.fields[i].error_messages = {'required': 'Campo obrigatorio'}
        
            self.fields[i].required = False
            
    class Meta:
        model = Services
        fields = '__all__'
        labels = {
            'client':('Cliente'),
        }
        
class MaterialsForm(forms.ModelForm):
     class Meta:
        model = Materials
        fields = '__all__'       
        
class PaymentsForm(forms.ModelForm):
     class Meta:
        model = Payments
        fields = '__all__'   