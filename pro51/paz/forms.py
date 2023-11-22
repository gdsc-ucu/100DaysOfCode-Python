from django import forms
from .models import UserProfile

class SignUpForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ['username', 'age', 'email']