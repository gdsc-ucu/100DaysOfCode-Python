from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/login', methods=['GET', 'POST'])

def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        if username == 'username' and password == 'password':
            return 'Login successful'
        else:
            return 'Login failed, check username and password'
    return render_template('nov-day48.html')

if __name__ == '__main__':
    app.run(debug=True)