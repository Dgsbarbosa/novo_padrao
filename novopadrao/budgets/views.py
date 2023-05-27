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
    
        
    
    form = BudgetsForm(request.user,request.POST)
    
    form_service = ServicesForm(request.POST)
    form_materials = MaterialsForm(request.POST)
    form_payment = PaymentsForm(request.POST)
    
    if form.is_valid()  :
        
        budget = form.save(commit=False)
        budget.user = request.user
        print('form :',budget)
        # budget.save()

        if form_service.is_valid():
            
            services = form_service.save(commit=False)
            # services.id_budget = budget
            print('form_service: ',services)
            #services.save()
            
        #     if form_payment.is_valid():
        #         contacts = form_payment.save(commit=False)
        #         contacts.client_id = client
                
        #         #contacts.save()
    
    
    context ={
        'form':form,
        'form_service':form_service,
        'form_materials':form_materials,
        'form_payment':form_payment,
        
        
        
    }
    return render(request, 'addBudgets.html', context)