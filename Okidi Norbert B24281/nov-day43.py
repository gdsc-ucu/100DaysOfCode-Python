from flask import Flask

app = Flask(__name__)

@app.route('/')

def hello_world():
    return 'Hello World'

if __name__ == '__main__':
    app.run(debug=True)

from django.shortcuts import HttpResponse

def home(request):
    return HttpResponse('Hello, world')