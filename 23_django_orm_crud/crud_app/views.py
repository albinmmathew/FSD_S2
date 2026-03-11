"""
Perform CRUD operations using Django ORM.
@ALBIN MAMMEN MATHEW
Roll No: 08 
Date: 23/01/2026
"""
from django.shortcuts import render, redirect, get_object_or_404
from .models import Student

def student_list(request):
    students = Student.objects.all()
    return render(request, 'crud_app/student_list.html', {'students': students})

def student_create(request):
    if request.method == "POST":
        Student.objects.create(
            first_name=request.POST.get('first_name'),
            last_name=request.POST.get('last_name'),
            roll_number=request.POST.get('roll_number'),
            email=request.POST.get('email')
        )
        return redirect('student_list')
    return render(request, 'crud_app/student_form.html')

def student_update(request, pk):
    student = get_object_or_404(Student, pk=pk)
    if request.method == "POST":
        student.first_name = request.POST.get('first_name')
        student.last_name = request.POST.get('last_name')
        student.roll_number = request.POST.get('roll_number')
        student.email = request.POST.get('email')
        student.save()
        return redirect('student_list')
    return render(request, 'crud_app/student_form.html', {'student': student})

def student_delete(request, pk):
    student = get_object_or_404(Student, pk=pk)
    if request.method == "POST":
        student.delete()
        return redirect('student_list')
    return render(request, 'crud_app/student_confirm_delete.html', {'student': student})
