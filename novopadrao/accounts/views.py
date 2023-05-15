from getpass import getuser
from site import getuserbase
from django.contrib.auth import get_user_model
from django.shortcuts import redirect, render
from django.contrib import messages


from .forms import CustomUserChangeForm, CustomUserCreationForm

from django.contrib.auth.decorators import login_required


def register(request):
    
    form = CustomUserCreationForm(request.POST)
    
    print(form)
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
    
    
    user_form = CustomUserCreationForm(instance=user)
  
  
    if(request.method == 'POST'):
        
        user_form = CustomUserCreationForm(request.POST,instance=user)
        
        if user_form.is_valid() :
            
            user_form.save()            
           
        return redirect('/accounts/perfil/user')
        
    
    context = {
        'user_form': user_form, 
        
        'user': user,
        
        }
    
    
    return render(request, 'company/editUser.html',context)