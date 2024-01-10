from flask import Flask

app = Flask(__name__)

@app.route('/')
def greeting():
    return 'Yo whats up, welcome to my Flask app!'

if __name__ == '__main__':
    app.run(debug=True)