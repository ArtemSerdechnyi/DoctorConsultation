from django.urls import path

from . import views


urlpatterns = [
    path('register_doctor/', views.register_doctor, name='register_doctor'),
    
]