
import datetime
from typing import Any, Dict, Mapping, Optional, Type, Union
from django import forms
from django.core.files.base import File
from django.db.models.base import Model
from django.forms.utils import ErrorList
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Field, HTML

from company.models import Clients
from .models import Budgets, Services, Materials, Payments


class BudgetsForm(forms.ModelForm):

    def __init__(self, user, *args, **kwargs):
        super(BudgetsForm, self).__init__(*args, **kwargs)

        for i in self.fields:

            self.fields[i].error_messages = {'required': 'Campo obrigatorio'}

            self.fields[i].required = False

            self.fields['client'].queryset = Clients.objects.filter(
                user_id=user)

        def numberBudget():

            number_budgets = 0

            number_budgets_last = Budgets.objects.values_list(
                'number_budgets').last()

            current_year = int(datetime.datetime.now().strftime("%Y"))

            if number_budgets_last:

                slice_budgets_last = number_budgets_last[0].split('-')

                number_budgets = int(slice_budgets_last[0])
                year_budgets = int(slice_budgets_last[1])

                if current_year != year_budgets:
                    number_budgets = 1

                elif current_year == year_budgets:
                    number_budgets = number_budgets + 1

            else:

                number_budgets = 1

            return f'{number_budgets:03d}-{current_year}'

        self.fields['number_budgets'].widget.attrs.update(
            {"value": f"{numberBudget()}"})

    class Meta:

        model = Budgets
        fields = [
            'number_budgets',
            'condition',
            'client',
            'reference',
            'validity',
            'term',
            'obs',

        ]
        labels = {
            'number_budgets': ('Numero do Pedido'),
            'client': ('Cliente'),
            'condition': ("Condicao"),
            'reference': ('Referencia'),
            'validity': ('Validade'),
            'term': ('Prazo de execucao'),
            'obs': ('Observacao')
        }
        widgets = {

            "number_budgets": forms.TextInput(attrs={

                'readonly': 'True',
                'size': '50%'


            }),
            
            "condition": forms.Select(attrs={
                'class': 'form-control'
            }),

            'validity': forms.NumberInput(attrs={
                'type': 'date',


            }),

            "obs": forms.Textarea(
                attrs={"cols": 80, "rows": 5}),
        }


class ServicesForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for i in self.fields:

            self.fields[i].error_messages = {'required': 'Campo obrigatorio'}

            self.fields[i].required = False
            
        self.helper = FormHelper()
        self.helper.layout = Layout(
            Field('descript'),
            Field('details'),
            Field('price'),
            Field('amount'),
            Field('total')
        )
            
        

    class Meta:

        model = Services
        fields = '__all__'

        exclude = ['id_budget']

        labels = {
            'descript': ('Descricao'),
            'details': ('Detalhes'),
            'price': ('Preco'),
            'amount': ('Quantidade'),

        }

        widgets = {

            'descript': forms.TextInput(attrs={

            }),

            'price': forms.TextInput(attrs={
                
                'type': 'text',
                

            }),



            "details": forms.Textarea(
                attrs={"cols": 80, "rows": 3}),

            'amount': forms.TextInput(attrs={
                


            }),

            'total': forms.TextInput(attrs={
                
                'readonly': 'True',


            }),



        }


class MaterialsForm(forms.ModelForm):
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

            
        self.helper = FormHelper()
        self.helper.layout = Layout(
            Field('descript'),
            Field('details'),
            Field('price'),
            Field('amount'),
            Field('total')
        )
            
       

    class Meta:
        model = Materials
        fields = '__all__'
        exclude = ['id_budget']
        
        labels = {
            
            'descript':'Descricao',
            'details': 'Detalhes',
            'price':'Preco',
            'amount': 'Quantidade',
            
        }
        
        
        widgets = {
            'descript': forms.TextInput(attrs={
                'id':'material-descript'

            }),

            'price': forms.TextInput(attrs={
                'id':'material-price',
                'type': 'text',
                

            }),



            "details": forms.Textarea(
                attrs={
                    "cols": 80, 
                    "rows": 3,
                    "id":"material-details"
                    }),

            'amount': forms.TextInput(attrs={
                

                'id':'material-amount'
            }),

            'total': forms.TextInput(attrs={
                'id': 'material-total',
                'readonly': 'True',

            }),

            
        }

    
class PaymentsForm(forms.ModelForm):
    class Meta:
        model = Payments
        fields = '__all__'
