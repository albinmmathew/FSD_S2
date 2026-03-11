"""
Create a Django app and configure it in the project.
@ALBIN MAMMEN MATHEW
Roll No: 08 
Date: 23/01/2026
"""
from django.http import HttpResponse

def home(request):
    return HttpResponse("Main App Configured Successfully!")
