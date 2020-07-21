from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
#this import will get the pre-made form from the django to the user for register. 
from django.contrib import messages
from .forms import UserRegisterForm, UserUpdateForm,ProfileUpdateForm

# Create your views here.
def register(request):
    if request.method == 'POST':
        form=UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username=form.cleaned_data.get('username')
            messages.success(request,f'Your accout has been created! Your are now able to logIn.')
            return redirect('login')
    else:
        form=UserRegisterForm()
    
    #we can only pass dictnary from this def function son at the end of the return there will be always a value represting the dictnary or dictnary itself.  
    return render(request,'users/register.html',{'form':form})


@login_required
def profile(request):
    if request.method=="POST":
        u_form=UserUpdateForm(request.POST,instance=request.user)
        p_form=ProfileUpdateForm(request.POST,request.FILES,instance=request.user.profile)
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request,f'Your account has been updated')
            return redirect('profile')
    else:
        u_form=UserUpdateForm(instance=request.user)
        p_form=ProfileUpdateForm(instance=request.user.profile)
    context={
        'u_form':u_form,
        'p_form':p_form
    }
    return render(request,'users/profile.html',context)
