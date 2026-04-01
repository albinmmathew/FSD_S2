"""
Create simple online feedback system with database integration.
@ALBIN MAMMEN MATHEW
Roll No: 08 
Date: 13/02/2026
"""
from django.shortcuts import render, redirect
from .forms import FeedbackForm

def feedback_view(request):
    if request.method == 'POST':
        form = FeedbackForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('success')
    else:
        form = FeedbackForm()
    return render(request, 'feedback_app/feedback_form.html', {'form': form})

def success_view(request):
    return render(request, 'feedback_app/success.html')
