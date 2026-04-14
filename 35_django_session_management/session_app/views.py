"""
Implement session management in Django.
@ALBIN MAMMEN MATHEW
Roll No: 08 
Date: 20/02/2026
"""
from django.shortcuts import render, redirect
from .models import ActiveSessionUser

def session_home(request):
    # Fix: Only increment if this is a main page request (not a favicon/static request)
    # Most browsers hit the root twice, so we track if we've already counted this specific visit
    if not request.session.get('counted_this_request', False):
        count = request.session.get('visit_count', 0)
        request.session['visit_count'] = count + 1
        request.session['counted_this_request'] = True

    # Custom data logic
    user_name = request.session.get('user_name', 'Guest')
    
    if request.method == 'POST':
        name = request.POST.get('name')
        if name:
            request.session['user_name'] = name
            # Global tracking: Save to database so everyone can see who is here
            ActiveSessionUser.objects.update_or_create(
                name=name,
                defaults={'name': name}
            )
            return redirect('session_home')
            
    # Get all "Active" users from the DB to show "who all are using sessions"
    all_users = ActiveSessionUser.objects.all().order_by('-last_seen')[:5]
            
    context = {
        'visit_count': request.session['visit_count'],
        'user_name': user_name,
        'all_users': all_users
    }
    # Reset the guard for the NEXT page load
    request.session['counted_this_request'] = False
    return render(request, 'session_app/session_home.html', context)

def clear_session(request):
    request.session.flush()
    return redirect('session_home')
