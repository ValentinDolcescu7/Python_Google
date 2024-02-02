from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth import update_session_auth_hash
from django.shortcuts import render, redirect
from .forms import ChangePasswordForm

# Create your views here.

@login_required
def change_password(request):
    """ Change user's password """

    # User reached route via POST
    if request.method == 'POST':
        form = ChangePasswordForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user) 
            messages.success(
                request, 'Your password was successfully updated!')
            return redirect('/')
        else:
            messages.error(request, 'Please correct the errors below.')
    
    # User reached route via GET
    else:
        form = ChangePasswordForm(request.user)
        
    return render(request=request, template_name='accounts/change_password.html', context={'form': form})
