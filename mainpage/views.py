from django.shortcuts import render
from .forms import UserRegistrationForm, profileForm
from django.contrib.auth.models import User
from django.views import generic
from datetime import datetime

from mainpage import models
from .models import Profile

def profile(request):
    return render(request, 'user_detail.html')

def index(request):
    return render(request, 'index.html')

def register(request):
    if request.method == 'POST':
        user_form = UserRegistrationForm(request.POST)
        profile_form = profileForm(request.POST)
        if user_form.is_valid() and profile_form.is_valid:
            # Create a new user object but avoid saving it yet
            new_user = user_form.save(commit=False)
            # Set the chosen password
            new_user.set_password(user_form.cleaned_data['password'])
            # Save the User object
            
            profile = profile_form.save(commit=False)
            profile.user = new_user
            new_user.save()
            profile.save()
            return render(request, 'register_done.html', {'profile': profile.user })
    else:
        user_form = UserRegistrationForm()
        profile_form = profileForm()
    return render(request, 'register.html', {'user_form': user_form, 'profile_form':profile_form })

