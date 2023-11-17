from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def profile(request, username):
    userdata = getuserData(username)
    return render(request, 'profile.html', {userdata})