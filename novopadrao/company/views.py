from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.http import HttpResponse
from .forms import  AddressForm, ClientForm, ContactsForm
from django.contrib import messages
import datetime

from .models import Address, Clients, Contacts
from accounts.models import PerfilCompany 

# Create your views here.

def home(request):
    
    
    return render(request, 'company/home.html')

@login_required
def listClients(request):
    
    search = request.GET.get('search')
    filter = request.GET.get('filter')
    
    if search:
                
        clients = Clients.objects.filter(nome__icontains=search, user=request.user)
        
    elif filter:
        clients = Clients.objects.filter(client_type=filter, user=request.user)
        
        
        
    else:
        clients_list = Clients.objects.all().order_by('-create_at').filter(user=request.user)
        
        
        paginator = Paginator(clients_list,3)
        page = request.GET.get('page')
        
        clients = paginator.get_page(page)
    
    clientsCount = Clients.objects.all().filter(user=request.user).count()
    
    context = {
        'clients': clients , 
        'clientsCount':clientsCount}
    
    return render(request, 'company/listclients.html', context)

@login_required
def  clientView(request, id):
    
    client = Clients.objects.get(pk=id) 
    
    try:
        address = Address.objects.get(client_id=client)
        
    except:
        address = ""
    
    try:
        contacts = Contacts.objects.get( client_id=client.id)
        
    except:
        contacts = ""

    print('client: ', client)
    print('address: ', address)
    print('contacts:',contacts )
    
    
    
    context = {
        'address':address,
        'contacts':contacts,
        'client': client,
        
        }
    
    return render(request, 'company/client.html', context)


@login_required
def newClient(request):
    
    form_clients = ClientForm(request.POST)        
    form_address = AddressForm(request.POST)    
    form_contacts = ContactsForm(request.POST)
    
    
    if form_clients.is_valid()  :
        
        client = form_clients.save(commit=False)
        client.user = request.user
        client.save()

        if form_address.is_valid():
            
            address = form_address.save(commit=False)
            address.client_id = client
            address.save()
            
            if form_contacts.is_valid():
                contacts = form_contacts.save(commit=False)
                contacts.client_id = client
                contacts.save()
                
            else:
                print('error')
                
            
        
        
        return redirect('/clients')
    
    else:
        form_clients = ClientForm()
        form_address = AddressForm()    
        form_contacts = ContactsForm()
        
       
    
    context = {
               'form_clients':form_clients,
               'form_address':form_address,
               'form_contacts':form_contacts, 
               }
    
    return render(request, 'company/addclient.html', context )

@login_required
def editClient(request, id):
    
    client = get_object_or_404(Clients, pk=id)
    
    
    client_form = ClientForm(instance=client)
    
    try:
        address = get_object_or_404(Address, client_id=client)
        
        address_form = AddressForm(instance=address)
        
        
    except:
         address_form = AddressForm()
         
    try:
        
        contacts = get_object_or_404(Contacts, client_id=client.id)
        contacts_form = ContactsForm(instance=contacts)
        
       
    except:
        contacts_form = ContactsForm(request.POST)
        
        
            
    
    if(request.method == 'POST'):
        
        client_form = ClientForm(request.POST,instance=client)
        
        if client_form.is_valid() :
            
            client_form.save()            
        
        try:
            contacts_form = ContactsForm(request.POST,instance=contacts)
            contacts_form.save() 
           
        except: 
                   
            if contacts_form.is_valid():
                contacts = contacts_form.save(commit=False)
                contacts.client_id = client
                contacts.save()  
            
            else:
                messages.info(request, 'Verifique os campos e tente novamente')
                return redirect(f'/clients/edit/{client.id}')
                
                
            
        try:
            address_form = AddressForm(request.POST,instance=address)
            address_form.save()
            
        
        except: 
            if address_form.is_valid():
                address = address_form.save(commit=False)
                address.client_id = client
                address.save()  
                
                
            
               
            
                   
        return redirect('/clients')
        
    
    context = {
        'client_form': client_form, 
        'address_form':address_form,
        'contacts_form':contacts_form,
        'client': client,
        
        }
    
    return render(request, 'company/editclient.html', context)

@login_required
def deleteClient(request, id):
    client = get_object_or_404(Clients, pk=id)
    client.delete()
    messages.info(request, 'Cliente deletado com sucesso.')

    return redirect('/clients')


