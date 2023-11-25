from flask import Flask
from django.shortcuts import HttpResponse
app = Flask(__name__)

@app.route('/')

def hello_world():
    return 'Hello World'
def home(request):
    return HttpResponse('Hello, world')
if __name__ == '__main__':
    app.run(debug=True)



