import datetime
from getpass import getuser
from django.http import HttpResponse
from django.shortcuts import redirect, render
from .forms import BudgetsForm, ServicesForm, MaterialsForm, PaymentsForm
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

    if (request.method == 'POST'):
        
        form = BudgetsForm(request.user,request.POST)

        service_form_count = int(request.POST.get('service_form-TOTAL_FORMS'))
        
        print('service_form_count',service_form_count)
                     
        service_forms = [ServicesForm(request.POST, prefix=f'service_form_{i+1}') for i in range((service_form_count))]      
        
        print(service_forms) 
        
        
        form_materials = MaterialsForm(request.POST)
    
        form_payment = PaymentsForm(request.POST)
        
        
        
        if form.is_valid() :

            budget = form.save(commit=False)                  
            print('form :', budget)
            # budget.save()      
            
            service_objects = []
            service_forms_valid = True       
        
                
            for i, service_form in enumerate(service_forms):
                if service_form.is_valid():
                    service = service_form.save(commit=False)
                    service_objects.append(service)
                    print(f'service {i+1}:', service)
                    
                else:
                    service_forms_valid = False
                    print('service form invalid:', service_form.errors)
        
            if service_forms_valid:
                for service_form in service_objects:
                    service_form.id_budget = budget
                    # service_form.save()
              
            else:
                print('error')    
           
           
           
           
        return redirect('/budgets')
    
    else:
        form = BudgetsForm(request.user)
        
        service_forms = [ServicesForm(prefix=f'service_form_{i+1}') for i in range(1)]
        
        form_materials = MaterialsForm()

        form_materials = MaterialsForm()
    
        form_payment = PaymentsForm()
        
    context = {
        'form': form,
        'service_forms': service_forms,        
        'form_materials': form_materials,
        'form_payment': form_payment,



    }
    return render(request, 'addBudgets.html', context)
