"""
Protect views using login_required decorator.
@ALBIN MAMMEN MATHEW
Roll No: 08 
Date: 30/01/2026
"""
from django.shortcuts import render
from django.contrib.auth.decorators import login_required

def index(request):
    return render(request, 'secure_app/index.html')

@login_required
def dashboard(request):
    return render(request, 'secure_app/dashboard.html')
