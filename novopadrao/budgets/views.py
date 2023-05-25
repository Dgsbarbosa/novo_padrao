import datetime
from django.shortcuts import render
from .forms import BudgetsForm,ServicesForm, MaterialsForm, PaymentsForm
from django.contrib.auth.decorators import login_required
from .models import Budgets


# Create your views here.

@login_required
def listBudgets(request):
    
    
    
    return render(request, 'budgets.html')


@login_required

def addBudgets(request):
    
   
        
    
    form = BudgetsForm(request.POST)
    
    
   
   
    
    
    form_service = ServicesForm(request.POST)
    form_materials = MaterialsForm()
    form_payment = PaymentsForm()
    
    
    context ={
        'form':form,
        'form_service':form_service,
        'form_materials':form_materials,
        'form_payment':form_payment,
        
        
        
    }
    return render(request, 'addBudgets.html', context)