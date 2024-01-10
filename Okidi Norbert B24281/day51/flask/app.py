from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])

def user_form():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        email = request.form['email']
        age = request.form['age']

        return f"Hello, {username}! Your password is {password}. Your email is {email} and you are {age} years' old"
    
    
    return render_template('user_form.html')


if __name__ == '__main__':
    app.run(debug=True)