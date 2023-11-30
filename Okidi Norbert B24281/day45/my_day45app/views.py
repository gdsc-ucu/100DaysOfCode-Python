from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(request):
    return render(request, 'home.html')

def about(request):
    website_info = {
        'website_name': 'Django website',
        'description': 'This is my first Django web app.',

    }
    return render(request, 'about.html', website_info)
