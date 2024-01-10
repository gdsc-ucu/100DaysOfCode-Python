from django.urls import path
from .views import profile

urlpatterns = [
    path('user/<str:username>/', profile, name='profile'),
]