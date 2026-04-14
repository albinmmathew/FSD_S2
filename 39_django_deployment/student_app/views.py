"""
Deploy a full stack application on a free hosting platform.
@ALBIN MAMMEN MATHEW
Roll No: 08 
Date: 27/02/2026
"""
from django.shortcuts import render, redirect, get_object_or_404
from .models import Student

def student_list(request):
    students = Student.objects.all().order_by('-created_at')
    return render(request, 'student_app/student_list.html', {'students': students})

def student_add(request):
    if request.method == 'POST':
        roll_no = request.POST.get('roll_no')
        name = request.POST.get('name')
        email = request.POST.get('email')
        course = request.POST.get('course')
        if roll_no and name:
            Student.objects.create(roll_no=roll_no, name=name, email=email, course=course)
            return redirect('student_list')
    return render(request, 'student_app/student_form.html', {'action': 'Add New'})

def student_edit(request, pk):
    student = get_object_or_404(Student, pk=pk)
    if request.method == 'POST':
        student.roll_no = request.POST.get('roll_no')
        student.name = request.POST.get('name')
        student.email = request.POST.get('email')
        student.course = request.POST.get('course')
        student.save()
        return redirect('student_list')
    return render(request, 'student_app/student_form.html', {'student': student, 'action': 'Edit'})

def student_delete(request, pk):
    student = get_object_or_404(Student, pk=pk)
    if request.method == 'POST':
        student.delete()
        return redirect('student_list')
    return render(request, 'student_app/student_confirm_delete.html', {'student': student})
