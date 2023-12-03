from django.shortcuts import render
from .forms import LoginForm

def login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            return render(request, 'paz/success.html', {'username': username})
    else:
        form = LoginForm()

    return render(request, 'paz/login.html', {'form': form})