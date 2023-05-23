
from django import forms

from .models import Budgets,Services, Materials,Payments 


class BudgetsForm(forms.ModelForm):
    class Meta:
        model = Budgets
        fields = '__all__'
        labels = {
            'client':('Cliente'),
            
        }
        
class ServicesForm(forms.ModelForm):
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