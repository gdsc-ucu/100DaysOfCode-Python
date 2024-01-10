from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        return HttpResponse('Login successful for user: {}'.format(username))
    return render(request, 'login.html')