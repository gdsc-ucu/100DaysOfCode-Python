from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/signup', methods=['GET', 'POST'])

def signup():
    if request.method == 'POST':
        username = request.form['username']
        email = request.form['email']

        if not username or not email:
            return render_template('signup.html', error='Both username and email required.')
        
        username = "norbert"
        return render_template('signup_successful.html', username=username)
    
    return render_template('signup.html')


if __name__ == 'main':
    app.run(debug=True)