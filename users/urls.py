from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.register, name='register'),
    path('login/', views.session, name='login'),
    path('dashboard/', views.dashboard, name='dashboard')
]