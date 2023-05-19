
from site import getuserbase
from django.contrib.auth import get_user_model
from django.shortcuts import get_object_or_404, redirect, render
from django.contrib import messages
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth import update_session_auth_hash
from .models import  PerfilCompany, UpdateUserForm
from .forms import  CustomPerfilCompanyForm, CustomUserChangeForm, CustomUserCreationForm, CustomPerfilCompanyForm

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
   
    
    return render(request,'accounts/perfis.html')



@login_required
def perfilUser(request):
    user = request.user
    
    context = {
        'user':user
    }
    return render(request,'accounts/perfilUser.html',context)




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
    
    
    return render(request, 'accounts/editUser.html',context)

@login_required

def alterPassword(request):
    
    user = request.user    
    fullname = f'{user.first_name} {user.last_name}' 
  
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        form.fields['old_password'].label = 'Senha antiga'
        form.fields['new_password1'].label = 'Nova senha'
        form.fields['new_password2'].label = 'Confirme a senha'
        
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)  
            messages.success(request, 'Sua senha foi alterada com sucesso!')
            return redirect('/accounts/perfil/user/alterPassword')
        else:
            messages.info(request, 'Corrija o erro abaixo.')
            form.fields['old_password'].label = 'Senha antiga'
            form.fields['new_password1'].label = 'Nova senha'
            form.fields['new_password2'].label = 'Confirme a senha'
            
    else:
        form = PasswordChangeForm(request.user)
    
    form.fields['old_password'].label = 'Senha antiga'
    form.fields['new_password1'].label = 'Nova senha'
    form.fields['new_password2'].label = 'Confirme a senha'   
        
    
    form.error_messages['password_incorrect'] = 'Sua senha antiga esta incorreta. Por favor tente novamente'
    print()
    
    context = {
            'form' : form,
            'fullname' : fullname, 
            
        }
    return render(request, 'accounts/alterPassword.html',context)
    
@login_required
 
def deleteUser(request):
    
    
    return render(request, 'accounts/deleteUser.html')


@login_required
def perfilCompany(request):
    try:
        company = PerfilCompany.objects.get(user = request.user)    
    
        print(company.logo)
    except:
        company = ""
        print('error')
    context = {
        'company':company,
    }
    return render(request, 'accounts/perfilCompany.html', context)


@login_required

def addCompany(request):   
    
    
    if request.method == 'POST':
        form = CustomPerfilCompanyForm(request.POST, request.FILES)
        
        if form.is_valid()  :
          
            company = form.save(commit=False)
            company.user = request.user
            company.save()
            
            return redirect('/accounts/perfil/company/')
    
    else:
        form = CustomPerfilCompanyForm()
    
    context = {
        'form' : form,
    }
    return render(request,'accounts/addCompany.html', context )