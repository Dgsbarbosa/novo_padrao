from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.http import HttpResponse
from .forms import  ClientForm
from django.contrib import messages
import datetime

from .models import Address, Clients

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
        clients = Clients.objects.filter(tipo=filter, user=request.user)
        
        
        
    else:
        clients_list = Clients.objects.all().order_by('-create_at').filter(user=request.user)
        
        
        paginator = Paginator(clients_list,3)
        page = request.GET.get('page')
        
        clients = paginator.get_page(page)
    
    clientsCount = Clients.objects.all().count()
    
   
    
    return render(request, 'company/listclients.html', {'clients': clients , 'clientsCount':clientsCount})

@login_required
def  clientView(request, id):
    
    client = get_object_or_404(Clients, pk=id)
    form = ClientForm(instance=client)
    
    return render(request, 'company/client.html', {'form': form, 'client': client })


@login_required
def newClient(request):
    
    form_clients = ClientForm(request.POST)    
    
    
    # print("cliente:",form_clients)
    
    if form_clients.is_valid()  :
        
        ...
        
        return redirect('/clients')
    
    else:
        form_clients = ClientForm()
        
    
    context = {
               'form_clients':form_clients,
               }
    
    return render(request, 'company/addclient.html', context )

@login_required
def editClient(request, id):
    client = get_object_or_404(Clients, pk=id)
    form = ClientForm(instance=client)
    print("id:", id)
    if(request.method == 'POST'):
        
        form = ClientForm(request.POST, instance=client)
        
        if(form.is_valid()):
            client.save()
            messages.info(request, 'Cliente alterado com sucesso.')
            return redirect('/clients')
        else:
            return render(request, 'company/editclient.html', {'form': form, 'client' :client })
        
    
    
    return render(request, 'company/editclient.html', {'form': form, 'client': client })

@login_required
def deleteClient(request, id):
    client = get_object_or_404(Clients, pk=id)
    client.delete()
    messages.info(request, 'Tarefa deletada com sucesso.')

    return redirect('/clients')
