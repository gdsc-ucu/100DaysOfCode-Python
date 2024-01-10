from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def profile(request, username):
    user_data = {'username': username, 'useremail': f'{username}@gmail.com' }
    return render(request, 'profile.html', {'user_profile': user_data})