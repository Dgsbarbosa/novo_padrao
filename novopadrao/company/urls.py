from django.urls import include, path
from . import views

urlpatterns = [
    path('', views.home),
    
    path('clients/', views.listClients, name='clients-list'),
    
    path("clients/client/<int:id>", views.clientView, name="client-view"),
    
    path('clients/newclient/', views.newClient, name="new-client"),
    
    path('newclient/', views.newClient, name="new-client"),
    
    path('clients/edit/<int:id>', views.editClient, name = 'edit-client'),
    
    path('clients/delete/<int:id>', views.deleteClient, name="delete-client"),
    
    path('perfil/', views.perfil, name='perfil'),
    
    path('perfil/usuario', views.perfilUser, name='perfil-user')
    
    
    
    
    
    
]   
