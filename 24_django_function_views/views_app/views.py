"""
Create function-based views in Django.
@ALBIN MAMMEN MATHEW
Roll No: 08 
Date: 30/01/2026
"""
from django.shortcuts import render
from .models import Student

def student_view(request):
    students = Student.objects.all()
    return render(request, 'views_app/student_view.html', {'students': students})
