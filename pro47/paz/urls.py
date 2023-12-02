from django.urls import path
from . import views
from .views import profile

urlpatterns = [
    path('home/', views.home, name='home'),
    path('user/<str:username>/', views.profile, name='profile'),
]