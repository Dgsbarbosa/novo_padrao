
from site import getuserbase
from django.contrib.auth import get_user_model
from django.shortcuts import get_object_or_404, redirect, render
from django.contrib import messages
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth import update_session_auth_hash
from .models import UpdateUserForm
from .forms import CustomUserChangeForm, CustomUserCreationForm, CustomUserEditForm

from django.contrib.auth.decorators import login_required


def register(request):
    
    form = CustomUserCreationForm(request.POST)
    
    
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)       
        
        
        if form.is_valid():
            form.save()
            return redirect('/')
    else:
        form = CustomUserCreationForm()


    return render(request, 'registration/register.html', {'form': form})


@login_required
def perfil(request):
   
    
    return render(request,'company/perfis.html')

@login_required
def perfilUser(request):
    user = request.user
    
    context = {
        'user':user
    }
    return render(request,'company/perfilUser.html',context)


@login_required
def editUser(request):
         
    user = request.user
    
    fullname = f'{user.first_name} {user.last_name}'
    fullname = fullname.title()    
   
    user_form = UpdateUserForm(instance=user)   

    if(request.method == 'POST'): 
               
        user_form = UpdateUserForm(request.POST,instance=user)              
            
        if user_form.is_valid() :
            
            user_form.save()  
            messages.info(request,'Usuario alterado com sucesso') 
            return redirect('/accounts/perfil/user/edit')        
                
    context = {
        'user_form': user_form, 
        'user':user,
        'fullname' :fullname
       
        }
    
    
    return render(request, 'company/editUser.html',context)

def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)  
            messages.success(request, 'Your password was successfully updated!')
            return redirect('change_password')
        else:
            messages.error(request, 'Please correct the error below.')
    else:
        form = PasswordChangeForm(request.user)
    return render(request, 'accounts/change_password.html', {
        'form': form
    })