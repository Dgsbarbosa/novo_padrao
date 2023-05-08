from django.urls import path
from . import views

urlpatterns = [
    path('', views.home),
    
    path('clients/', views.listClients, name='clients-list'),
    
    path("clients/client/<int:id>", views.clientView, name="client-view"),
    
    path('clients/newclient/', views.newClient, name="new-client"),
    
    path('newclient/', views.newClient, name="new-client"),
]   
