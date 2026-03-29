"""
Create a role-based authentication system using Django.
@ALBIN MAMMEN MATHEW
Roll No: 08 
Date: 13/02/2026
"""
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required, user_passes_test

def is_admin(user):
    return user.profile.role == 'admin'

def is_manager(user):
    return user.profile.role == 'manager'

def is_user(user):
    return user.profile.role == 'user'

@login_required
def home(request):
    if request.user.profile.role == 'admin':
        return redirect('admin_dashboard')
    elif request.user.profile.role == 'manager':
        return redirect('manager_dashboard')
    elif request.user.profile.role == 'user':
        return redirect('user_dashboard')
    return render(request, 'roles_app/home.html')

@login_required
@user_passes_test(is_admin, login_url='unauthorized')
def admin_dashboard(request):
    return render(request, 'roles_app/admin_dashboard.html')

@login_required
@user_passes_test(is_manager, login_url='unauthorized')
def manager_dashboard(request):
    return render(request, 'roles_app/manager_dashboard.html')

@login_required
@user_passes_test(is_user, login_url='unauthorized')
def user_dashboard(request):
    return render(request, 'roles_app/user_dashboard.html')

def unauthorized(request):
    return render(request, 'roles_app/unauthorized.html')
