from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.http import HttpResponse
from .forms import ClientForm
from django.contrib import messages
import datetime

from .models import Clients

# Create your views here.
def home(request):
    return render(request, 'company/home.html')


def listClients(request):
    
    search = request.GET.get('search')
    
    if search:
        
        clients = Clients.objects.filter(nome__icontains=search)
        
    else:
        clients_list = Clients.objects.all().order_by('-create_at')
        paginator = Paginator(clients_list,3)
        page = request.GET.get('page')
        
        clients = paginator.get_page(page)
    
    clientsCount = Clients.objects.all().count()
    
    print
    
    return render(request, 'company/listclients.html', {'clients': clients , 'clientsCount':clientsCount})


def  clientView(request, id):
    
    client = get_object_or_404(Clients, pk=id)
    form = ClientForm(instance=client)
    
    
    
                 
    return render(request, 'company/client.html', {'form': form, 'client': client })


def newClient(request):
    
    form = ClientForm(request.POST)
    
    if form.is_valid():
        client = form.save(commit=False)
        client.save()
        return redirect('/clients')
    
    else:
        form = ClientForm()
        
    return render(request, 'company/addclient.html', {'form':form} )


def editClient(request, id):
    client = get_object_or_404(Clients, pk=id)
    form = ClientForm(instance=client)
    
    if(request.method == 'POST'):
        
        form = ClientForm(request.POST, instance=client)
        
        if(form.is_valid()):
            client.save()
            return redirect('/clients')
        else:
            return render(request, 'company/editclient.html', {'form': form, 'client' :client })
        
    
                 
    return render(request, 'company/editclient.html', {'form': form, 'client': client })


def deleteClient(request, id):
    client = get_object_or_404(Clients, pk=id)
    client.delete()
    messages.info(request, 'Tarefa deletada com sucesso.')

    return redirect('/clients')
