from flask import Flask, render_template, request
from flask_caching import Cache
from flask_compress import Compress

app = Flask(__name__)

cache = Cache(app, config={'CACHE_TYPE': 'simple'})
Compress(app)


@app.route('/')

def signup():
    return render_template('signup.html')

@app.route('/signup', methods=['POST'])
def sign():
    username = request.form['username']
    email = request.form['email']
    if not username or not email:
        return "Failure: Both username and email required."

    return render_template("signup_successful.html")


if __name__ == '__main__':
    app.run(debug=True)