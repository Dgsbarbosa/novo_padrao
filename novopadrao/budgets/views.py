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
    
    number_budgets_last = Budgets.objects.values_list('number_budgets').last()
    
    year = datetime.datetime.now().strftime("%Y")
    

    if number_budgets_last:
    #.order_by('-number_budgets').values()
        
        print(number_budgets_last)
    else:
        
        number_budgets = f'001-{year}'
        print(number_budgets)
        
        
    
    form = BudgetsForm(request.POST,)
    
    form.number_budgets = number_budgets
    print(form.number_budgets)
   
    
    
    form_service = ServicesForm(request.POST)
    form_materials = MaterialsForm()
    form_payment = PaymentsForm()
    
    
    context ={
        'form':form,
        'form_service':form_service,
        'form_materials':form_materials,
        'form_payment':form_payment,
        'form.number_budgets':form.number_budgets
        
        
    }
    return render(request, 'addBudgets.html', context)