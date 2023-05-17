from django.urls import path, reverse_lazy

from . import views

urlpatterns = [
    path('register/', views.register, name="register"),
    
    path('perfil/', views.perfil, name='perfil'),
    
    path('perfil/user/', views.perfilUser, name='perfil-user'),
    
    path('perfil/user/edit', views.editUser, name='perfil-edit'),
    
    path('perfil/user/alterPassword', views.alterPassword, name='alter-password'),
    
    path('perfil/user/delete', views.deleteUser, name='delete-user'),
    
    
    
]
