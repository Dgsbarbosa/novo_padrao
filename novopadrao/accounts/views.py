from django.shortcuts import redirect, render

from .forms import CustomUserChangeForm, CustomUserCreationForm

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
