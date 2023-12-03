from django.shortcuts import render
from signupapp.forms import signupForm

# Create your views here.
def signup(request):
    if request.method == 'POST':
        form = signupForm(request.POST)
        if form.is_valid():
            return render(request, 'signup_success.html')
    else:
        form = signupForm()
    return render(request, 'signup.html', {'form': form})
