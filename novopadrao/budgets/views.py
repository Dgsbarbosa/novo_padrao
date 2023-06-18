
import datetime
from getpass import getuser
from django.http import HttpResponse
from django.shortcuts import redirect, render


from .forms import BudgetsForm, ServicesForm, MaterialsForm, PaymentsForm, TotalsForms
from django.contrib.auth.decorators import login_required
from .models import Budgets, Materials, Payments, Services, Totals
from django.contrib.auth import get_user_model
from django.core.paginator import Paginator
from django.contrib import messages
from accounts.models import PerfilCompany
from company.models import Clients, Address, Contacts
from accounts.models import CustomUser

from . import add_budget

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
        budgets = Budgets.objects.filter(situation=filter, user=request.user).order_by('-create_at').filter(user = request.user)
        
        
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
    
    
        # Calculando totais
    budget = Budgets.objects.get(id=19)

    
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
            budget.user = request.user 
                         
            budget.save()
            
            print('budget:', budget)
            
            service_objects = []
            service_forms_valid = True              
                
            for i, service_form in enumerate(service_forms):
                if service_form.is_valid():
                    service = service_form.save(commit=False)
                    service_objects.append(service)
                    
                else:
                    service_forms_valid = False
                    

            if service_forms_valid:
                for i, service_form in enumerate( service_objects):
                    service_form.id_budget = budget
                    
                    service_form.save()
                    
                    print(f'service {i +1}: {service_form} ')
                            
            
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
                    for i, material_obj in enumerate( material_objects):
                        material_obj.id_budget = budget
                        
                        material_obj.save()
                        
                        print(f'material {i +1}: {material_obj}')
                
                    if payment_forms.is_valid():
                        payment = payment_forms.save(commit=False)
                                        
                        payment.id_budget = budget
                        
                        payment.save()
                        
                        print('pagamento: ',payment)
                        
                        
                        total_services = request.POST.get('total_services')
                        
                        total_materials = request.POST.get('total_materials')
                        total_discount = request.POST.get('total_discount')

                        total_condition = request.POST.get('total_condition')
                        
                        total_budgets = request.POST.get('total_budget')
                        
                        # grava o valor de totais no banco de dados
                        
                        total = Totals(id_budget = budget, total_services = total_services, total_materials = total_materials, discount = total_discount, parcels = total_condition, total_final = total_budgets)
                        total.save()
                        print('total:', total)
                    
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
    # 'total_services': total_services,
    # 'total_materials':total_materials,
    }   
    
    return render(request, 'addBudgets.html', context)


def viewBudget(request, id):
    
    #get no perfil da empresa
    try:
        perfilCompany = PerfilCompany.objects.get(pk=request.user.id) 
    except:
        perfilCompany = "Orcamento de servicos"
    
    
    # pega o orçamento
    budget = Budgets.objects.get(pk=id)

    #  pega o endereço do cliente
    try:
        addressClient = Address.objects.get(client_id=budget.client.id)
    except:
        addressClient = ""

    #  pega o contato do cliente
    try:
        contactsClient = Contacts.objects.get(client_id = budget.client.id)
    except:
        contactsClient=""
        
    # pega os serviços
    try:
        services = Services.objects.filter(id_budget = budget.id)
        
        
    except:
        services = ""
        
        print('error')
        
    # pega os materiais
    
    try:    
        materials = Materials.objects.filter(id_budget = budget.id)
    except:
        materials = ""
        
        
    try:
        total = Totals.objects.filter(id_budget = budget.id)
    except:
        total = ""
        
    payments = Payments.objects.filter(id_budget = budget.id)
    print("id:",budget.id)

        
    print('perfilCompany: ', perfilCompany)
    print("budget: ", budget)
    print('addressClient:', addressClient)
    print('contactsClient:', contactsClient)
    print("services:", services)
    print('materials:', materials)
    print('total:', total)
    print('payments:', payments)
    
    context = {
        'perfilCompany': perfilCompany,
        'budget': budget,
        'addressClient': addressClient,
        'contactsClient': contactsClient,
        'services': services,
        'materials': materials,
        'total': total,
        'payments': payments,
        
        }
    return render(request, 'viewBudget.html',context)