from django.urls import path
from . import views,about

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', about, name='about'),
]