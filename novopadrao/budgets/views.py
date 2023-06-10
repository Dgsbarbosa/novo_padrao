
import datetime
from getpass import getuser
from django.http import HttpResponse
from django.shortcuts import redirect, render
from .forms import BudgetsForm, ServicesForm, MaterialsForm, PaymentsForm
from django.contrib.auth.decorators import login_required
from .models import Budgets
from django.contrib.auth import get_user_model
from django.core.paginator import Paginator
from django.contrib import messages

from company.models import Clients
from accounts.models import CustomUser

# Create your views here.


@login_required
def listBudgets(request):
   
    search = request.GET.get('search')
    filter = request.GET.get('filter-budgets')
    
    print(filter)
    
    if search:
                
        budgets = Budgets.objects.filter(client__name__icontains=search, user=request.user) or Budgets.objects.filter(number_budgets__icontains=search, user=request.user)
        
        if not budgets: 
            messages.warning(request,"Sem resultados.")
            
        
    elif filter:
        budgets = Budgets.objects.filter(condition=filter, user=request.user)
        
        
        if not budgets: 
            messages.warning(request,"Sem resultados.")
            
        
        
        
    else:
        budgets = Budgets.objects.all().order_by('-create_at').filter(user = request.user)
        
    if budgets:
        paginator = Paginator(budgets,3)
        page = request.GET.get('page')
        
        budgets = paginator.get_page(page)
    
    
    budgetsCount = Budgets.objects.all().filter(user=request.user).count()
    
    
    context = {
        'budgets': budgets , 
        'budgetsCount':budgetsCount}
    
    return render(request, 'budgets.html', context)
    



@login_required
def addBudgets(request):
    
    if (request.method == 'POST'):
        
        # Form dados basico
        form = BudgetsForm(request.user,request.POST)

        # Form services
        service_form_count = int(request.POST.get('service_form-TOTAL_FORMS'))
        
                                            
        service_forms = [ServicesForm(request.POST, prefix=f'service_form_{i+1}') for i in range((service_form_count))]    
          
          
        #  Form materials
        material_form_count = int(request.POST.get('materials_form-TOTAL_FORMS'))
        
        material_forms = [MaterialsForm(request.POST, prefix=f'material_form_{i+1}') for i in range(material_form_count)]

        
        payment_forms = PaymentsForm(request.POST)
        
                
        if form.is_valid() :
            
            budget = form.save(commit=False)
            budget.user_id = request.user                  
            budget.save()
            
            service_objects = []
            service_forms_valid = True              
                
            for i, service_form in enumerate(service_forms):
                if service_form.is_valid():
                    service = service_form.save(commit=False)
                    service_objects.append(service)
                    
                else:
                    service_forms_valid = False
                    

            if service_forms_valid:
                for service_form in service_objects:
                    service_form.id_budget = budget
                    service_form.save()
                            
            
                #  Form budgets save
                material_objects = []
                material_form_valid = True
                
                
                for material_form in material_forms:
                    
                    if material_form.is_valid():
                                            
                        material = material_form.save(commit=False)
                        
                        material_objects.append(material)
                        
                        
                    else:
                        material_form_valid = False
                        
                        print('error')

                if material_form_valid:
                    for material_obj in material_objects:
                        material_obj.id_budget = budget
                        material_obj.save()
                        
        
                
                    if payment_forms.is_valid():
                        payment = payment_forms.save(commit=False)
                                        
                        payment.id_budget = budget
                        payment.save()
                        
        else:
            print('error')
        return redirect('/budgets')
    
    else:
        form = BudgetsForm(request.user)
        
        service_forms = [ServicesForm(prefix=f'service_form_{i+1}') for i in range(1)]
        
        material_forms = [MaterialsForm(prefix=f'material_form_{i+1}') for i in range(1)]
        
            
        payment_forms = PaymentsForm()
        
    
    context = {
    'form': form,
    'service_forms': service_forms,        
    'material_forms': material_forms,
    'payment_forms': payment_forms,


    }   
    
    return render(request, 'addBudgets.html', context)
