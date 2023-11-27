from flask import Flask, render_template, request


app = Flask(__name__)


@app.route('/')

def signup():
    return render_template('signup.html')

@app.route('/signup', methods=['POST'])
def sign():
    username = request.form['username']
    email = request.form['email']
    if not username or not email:
        return "Failure Both username and email required."

    return render_template("signup_successful.html")


if __name__ == 'main':
    app.run(debug=True)