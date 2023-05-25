
import datetime
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
            
        def numberBudget():
        
            number_budgets = 0            
            
            number_budgets_last = Budgets.objects.values_list('number_budgets').last()
            
            current_year = int(datetime.datetime.now().strftime("%Y"))
            
            if number_budgets_last:
                
                slice_budgets_last = number_budgets_last.split('-')
                number_budgets = int(slice_budgets_last[0])
                year_budgets = int(slice_budgets_last[1])
                                                
                if current_year != year_budgets:
                    number_budgets = 1
                    
                elif current_year == year_budgets:   
                    number_budgets = number_budgets + 1
                
            else:
                
                number_budgets = 1
            
            return f'{number_budgets:03d}-{current_year}'
             
        
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
            
            "number_budgets" : forms.TextInput(attrs={
                'value': f'{numberBudget()}',
                'disabled':'True',
                'size': '50%'
                

            }),
            
            "client": forms.Select(),
             
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