"""
Create a Django project and display Hello World on the browser.
@ALBIN MAMMEN MATHEW
Roll No: 08 
Date: 23/01/2026
"""
from django.http import HttpResponse

def index(request):
    return HttpResponse("Hello World")
