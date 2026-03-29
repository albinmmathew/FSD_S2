from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('admin-dash/', views.admin_dashboard, name='admin_dashboard'),
    path('manager-dash/', views.manager_dashboard, name='manager_dashboard'),
    path('user-dash/', views.user_dashboard, name='user_dashboard'),
    path('unauthorized/', views.unauthorized, name='unauthorized'),
]
