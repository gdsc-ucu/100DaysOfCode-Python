from django import forms

class SignupForm(forms.Form):
    username = forms.CharField(label='Username', required=True)
    email = forms.EmailField(label='Email', required=True)
    age = forms.CharField(label='Age', required=True)
