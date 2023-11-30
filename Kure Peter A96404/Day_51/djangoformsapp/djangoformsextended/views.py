from django.shortcuts import render
from djangoformsextended.forms import SignupForm


# Create your views here.
def signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            return render(request, 'signup_success.html', {
                'username': form.cleaned_data['username'],
                'email': form.cleaned_data['email'],
                'age': form.cleaned_data['age']
            })
    else:
        form = SignupForm()
    return render(request, 'signup.html', {'form': form})