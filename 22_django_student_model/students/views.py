"""
Create a Django model for Student and perform migrations. Register models in the Django admin panel
@ALBIN MAMMEN MATHEW
Roll No: 08 
Date: 23/01/2026
"""
from django.http import HttpResponse

def index(request):
    return HttpResponse("Student Model & Admin Panel Configured Successfully!")
