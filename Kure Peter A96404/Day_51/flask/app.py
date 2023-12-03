from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        username = request.form['username']
        email = request.form['email']
        age = request.form['age']
        return (f'Hello, {username}!<br>'
                f'Email: {email}<br>'
                f'Age: {age}<br>') 
    return render_template('signup.html')

if __name__ == '__main__':
    app.run(debug=True)
