from django.urls import path
from .views import user_form, success_page

urlpatterns = [
    path("user_form/", user_form, name='user_form'),
    path('success/', success_page, name='success_page'),
]