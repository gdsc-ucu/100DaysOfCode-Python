from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
users = {
    "clint_capella": {"name": "Clint Capella", "email": "clint@example.com"},
    "peter_kure": {"name": "Peter Kure", "email": "peter@example.com"},
    "sam_altman": {"name": "Sam Altman", "email": "sam@example.com"},
    "rey mysterio": {"name": "Rey Mysterio", "email": "reymysterio@example.com"}
}

def show_profile(request, username):
    user = users.get(username, None)
    if user:
        return render(request, 'profile.html', {'user': user})
    else:
        return HttpResponse("User not found", status=404)