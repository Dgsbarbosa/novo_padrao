
import datetime
from typing import Any, Dict, Mapping, Optional, Type, Union
from django import forms
from django.core.files.base import File
from django.db.models.base import Model
from django.forms.utils import ErrorList
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Field, HTML

from company.models import Clients
from .models import Budgets, Services, Materials, Payments, Totals


class BudgetsForm(forms.ModelForm):

    def __init__(self, user, *args, **kwargs):
        super(BudgetsForm, self).__init__(*args, **kwargs)

        for i in self.fields:

            self.fields[i].error_messages = {'required': 'Campo obrigatorio'}

            self.fields[i].required = False

            self.fields['client'].queryset = Clients.objects.filter(
                user_id=user).values_list('name', flat=True)

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
        self.fields['situation'].initial = 'Pendente'
    class Meta:

        model = Budgets
        fields = [
            'number_budgets',
            'situation',
            'client',
            'reference',
            'validity',
            'term',
            'obs',

        ]
        labels = {
            'number_budgets': ('Numero do Pedido'),
            'client': ('Cliente'),
            'situation': ("Situacao"),
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
            
            "situation": forms.Select(attrs={
                'class': 'form-control'
            }),

            'validity': forms.NumberInput(attrs={
                'type': 'date',


            }),

            "obs": forms.Textarea(
                attrs={"cols": 80, "rows": 2}),
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
    
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['discount'].choices = (
            ('none','Sem desconto'),
            ('valor', 'Valor'),
            ('porcentagem', 'Porcentagem')
        )
        self.fields['discount'].initial = 'none'
        
        self.fields['condition'].choices = (
            
            ('a vista','A vista'),
            ('sinal','Sinal'),
            ('parcelas','Parcelas'),
        )
        self.fields['condition'].initial = 'a vista'
        
        self.fields['methods'].choices = (
            ('dinheiro','Dinheiro'),
            ('pix','Pix'),
            ('tranferencia','Tranferencia'),
            ('credito','Cartao de credito'),
            ('debito','Cartao de debito'),
        )
        self.fields['methods'].initial = 'dinheiro'
        
    class Meta:
        model = Payments
        fields = '__all__'
        exclude = ['id_budget'] 
        
        labels = {
            'discount': "Desconto",
            'condition': 'Condicao de pagamento',
            'methods': "Metodos de pagamento"
        }
        
        widgets = {
            
            'discount': forms.RadioSelect(
                attrs={'class': 'form-control'},
                
            ),
            'condition': forms.RadioSelect(
                
            ),
            'methods': forms.RadioSelect(
                
            ),
            'obs': forms.Textarea(
                attrs={
                    'cols': 80,
                    'rows': 2,
                }
            )
            
            
        }
        
class TotalsForms(forms.ModelForm):
    
    class Meta:
        model = Totals 
        fields = '__all__'
    
