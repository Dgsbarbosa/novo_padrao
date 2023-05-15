from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.register, name="register"),
    
    path('perfil/', views.perfil, name='perfil'),
    
    path('perfil/user/', views.perfilUser, name='perfil-user'),
    
     path('perfil/user/edit', views.editUser, name='perfil-edit')
    
]
