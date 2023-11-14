from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def greet(request):
    return HttpResponse("Hello World, welcome to my Django app")

def about(request):
    return render(request,'about.html')