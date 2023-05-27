import datetime
from getpass import getuser
from django.shortcuts import render
from .forms import BudgetsForm,ServicesForm, MaterialsForm, PaymentsForm
from django.contrib.auth.decorators import login_required
from .models import Budgets
from django.contrib.auth import get_user_model

from company.models import Clients
from accounts.models import CustomUser

# Create your views here.

@login_required
def listBudgets(request):
    
   
    return render(request, 'budgets.html')


@login_required

def addBudgets(request):
    
  
    client = Clients.objects.filter(user_id=request.user)
    # print(client)
    form = BudgetsForm(request.POST,instance=request.user)
    
    
    
   
   
    
    
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