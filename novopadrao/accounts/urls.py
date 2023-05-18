from django.urls import path, reverse_lazy

from . import views

from django.contrib.auth.views import (
    LogoutView, 
    PasswordResetView, 
    PasswordResetDoneView, 
    PasswordResetConfirmView,
    PasswordResetCompleteView
)

urlpatterns = [
    path('register/', views.register, name="register"),
    
    path('perfil/', views.perfil, name='perfil'),
    
    path('perfil/user/', views.perfilUser, name='perfil-user'),
    
    path('perfil/user/edit', views.editUser, name='perfil-edit'),
    
    path('perfil/user/', views.perfilUser, name='perfil-user'),
    
    path('perfil/user/edit', views.editUser, name='perfil-edit'),
    
    path('perfil/user/alterPassword', views.alterPassword, name='alter-password'),
    
    path('perfil/user/delete', views.deleteUser, name='delete-user'),
    
    
    
    path('passwords/password-reset/', 
     PasswordResetView.as_view(
        template_name='passwords/password_reset.html',
        html_email_template_name='passwords/password_reset_email.html'
    ),
    name='password-reset'
),
    
    path('password_reset/done/', PasswordResetDoneView.as_view(template_name='passwords/password_reset_done.html'),name='password_reset_done'),
    
    path('password-reset-confirm/<uidb64>/<token>/', PasswordResetConfirmView.as_view(template_name='passwords/password_reset_confirm.html'),name='password_reset_confirm'),
    
    path('password-reset-complete/',PasswordResetCompleteView.as_view(template_name='passwords/password_reset_complete.html'),name='password_reset_complete'),
    
    
    path('perfil/company/', views.perfilCompany, name='perfil-user'),
   
    
]
