from django import forms
class signupForm(forms.Form):
    username = forms.CharField(required=True)
    email = forms.EmailField(required=True)