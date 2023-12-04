from django.shortcuts import render
from django.http import HttpResponse

def signup(request):
    if request.method == 'POST':
        username = request.POST.get('username', '')
        email = request.POST.get('email', '')

        if not username or not email:
            return render(request, 'signup.html', {'error':'Both username and email required.'})
    
        return render(request, 'signup_successful.html', {'username': username})
    return render(request, 'signup.html')


