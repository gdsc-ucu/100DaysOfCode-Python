from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.


def login(request):
    
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        if username == 'username' and password == 'password':
            return HttpResponse('Login successful')
        else:
            return HttpResponse('Login failed, check username and password')
        
    return render(request, 'nov-day48.html')
