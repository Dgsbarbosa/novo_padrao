from django.shortcuts import render
from django.http import HttpResponse

from .models import Clients

# Create your views here.
def home(request):
    return render(request, 'company/home.html')


def listClients(request):
    
    clients = Clients.objects.all()
    
    
    return render(request, 'company/listclients.html', {clients : clients})
