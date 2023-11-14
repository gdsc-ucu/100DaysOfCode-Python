from django.urls import path
from .views import show

urlpatterns=[
    path('', show, name='hello_world'),
]