from django.shortcuts import render, redirect
from .forms import SignUpForm

def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            # Save the form data to the database or perform other actions
            # For simplicity, let's just print the data for now
            print(form.cleaned_data)
            return render(request, 'paz/success.html', {'data': form.cleaned_data})
    else:
        form = SignUpForm()

    return render(request, 'paz/signup.html', {'form': form})