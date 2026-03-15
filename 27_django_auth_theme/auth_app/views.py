"""
Create a Django login and logout system Implement dark mode and light mode toggle using HTML and CSS.
@ALBIN MAMMEN MATHEW
Roll No: 08 
Date: 30/01/2026
"""
from django.shortcuts import render
from django.contrib.auth.decorators import login_required

@login_required
def home(request):
    return render(request, 'auth_app/home.html')
