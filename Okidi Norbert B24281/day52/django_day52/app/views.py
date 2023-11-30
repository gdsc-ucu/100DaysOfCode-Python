from django.shortcuts import render, redirect
from django import forms

class UserForm(forms.Form):
    username = forms.CharField(max_length=100)
    email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput)

    def clean_password(self):
        password = self.cleaned_data.get('password')
        if len(password) < 6:
            raise forms.ValidationError("Password entered must be atleast 6 characters long")
        
        return password
    
def success_page(request):
     return render(request, 'success.html')
    

def user_form(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        
        if form.is_valid():
            print("form is valid processing----")
            return redirect('success_page')
        else:
            print("form invalid")
    else:
     form = UserForm()

    return render(request, 'user_form.html', {'form':form})