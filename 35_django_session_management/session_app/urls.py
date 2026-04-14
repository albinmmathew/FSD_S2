from django.urls import path
from . import views

urlpatterns = [
    path('', views.session_home, name='session_home'),
    path('clear/', views.clear_session, name='clear_session'),
]
