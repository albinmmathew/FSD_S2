"""
Create class-based views in Django.
@ALBIN MAMMEN MATHEW
Roll No: 08 
Date: 30/01/2026
"""
from django.views.generic import ListView
from .models import Student

class StudentListView(ListView):
    model = Student
    template_name = 'cbv_app/student_list.html'
    context_object_name = 'students'
