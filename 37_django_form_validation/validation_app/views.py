"""
Implement form validation and error handling in Django.
@ALBIN MAMMEN MATHEW
Roll No: 08 
Date: 27/02/2026
"""
from django.shortcuts import render, redirect
from .forms import UserProfileForm

def profile_create_view(request):
    if request.method == 'POST':
        form = UserProfileForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'validation_app/success.html')
    else:
        form = UserProfileForm()
    
    return render(request, 'validation_app/profile_form.html', {'form': form})
