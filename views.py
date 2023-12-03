from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return HttpResponse("Hello, welcome to my Django app!")

def about(request):
    return render(request, 'view.html', {'zzi': 'My Django Website'})
