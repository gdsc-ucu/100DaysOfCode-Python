from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return render(request, 'paz/home.html')

def profile(request, username):
    return render(request, 'paz/profile.html', {'username': username})