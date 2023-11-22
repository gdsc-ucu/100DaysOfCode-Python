from django import forms

class SignUpForm(forms.Form):
    username = forms.CharField(max_length=50, required=True)
    age = forms.IntegerField(required=True)
    email = forms.EmailField(required=True)
    password = forms.CharField(widget=forms.PasswordInput(), required=True, min_length=8)