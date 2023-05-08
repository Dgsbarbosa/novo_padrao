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
    
    clients = Clients.objects.all()
    # print("count: ",clients.count())
    
    return render(request, 'company/listclients.html', {'clients': clients})


def  clientView(request, id):
    client = Clients.objects.get(pk=id)
    if client.tipo == "1":
        client.tipo = "Fisica"   
    elif client.tipo == "2":
        client.tipo = "Juridica"
    print(client.tipo)
    return render(request, 'company/client.html', {'client': client})


def newClient(request):
    
    form = ClientForm(request.POST)
    
    if form.is_valid():
        client = form.save(commit=False)
        client.save()
        return redirect('/')
    
    else:
        form = ClientForm()
        
    return render(request, 'company/addclient.html', {'form':form} )
