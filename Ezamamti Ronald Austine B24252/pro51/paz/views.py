from django.shortcuts import render
from django.http import HttpResponse
from .forms import SignUpForm

def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            age = form.cleaned_data['age']
            email = form.cleaned_data['email']
            return HttpResponse(f' Successfully signed up as {username} of age {age} with email {email}')
    else:
        form = SignUpForm()

    return render(request, 'paz/signup.html', {'form': form})