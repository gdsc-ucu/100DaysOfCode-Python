from django import forms
from django.core.exceptions import ValidationError

class SignupForm(forms.Form):
    username = forms.CharField(label='Username', required=True)
    email = forms.EmailField(label='Email', required=True)
    password = forms.CharField(label='Password', widget=forms.PasswordInput, required=True)
    age = forms.CharField(label='Age', required=True)

    def clean_password(self):
        password = self.cleaned_data.get('password')
        if len(password) < 8:
            raise ValidationError('Password must be at least 8 characters long')
        return password
