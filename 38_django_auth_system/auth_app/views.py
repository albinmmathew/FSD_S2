"""
Create a secure authentication system with password hashing.
@ALBIN MAMMEN MATHEW
Roll No: 08 
Date: 27/02/2026
"""
from django.shortcuts import render, redirect
from .models import CUser

def signup_view(request):
    if request.method == 'POST':
        user_name = request.POST.get('username')
        email = request.POST.get('email')
        pass_word = request.POST.get('password')
        if user_name and email and pass_word:
            user = CUser(username=user_name, email=email)
            user.set_password(pass_word)
            user.save()
            return redirect('login')
    return render(request, 'auth_app/signup_custom.html')

def login_view(request):
    error = None
    if request.method == 'POST':
        user_name = request.POST.get('username')
        pass_word = request.POST.get('password')
        try:
            user = CUser.objects.get(username=user_name)
            if user.check_password(pass_word):
                request.session['user_id'] = user.id
                return redirect('dashboard')
            else:
                error = "Invalid password!"
        except CUser.DoesNotExist:
            error = "User not found!"
            
    return render(request, 'auth_app/login_custom.html', {'error': error})

def dashboard_view(request):
    user_id = request.session.get('user_id')
    if not user_id:
        return redirect('login')
    try:
        user = CUser.objects.get(id=user_id)
    except CUser.DoesNotExist:
        return redirect('login')
    return render(request, 'auth_app/dashboard_custom.html', {'user': user})

def logout_view(request):
    if 'user_id' in request.session:
        del request.session['user_id']
    return redirect('login')
