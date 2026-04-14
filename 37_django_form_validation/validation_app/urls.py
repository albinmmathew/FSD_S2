from django.urls import path
from . import views

urlpatterns = [
    path('', views.profile_create_view, name='profile_form'),
]
