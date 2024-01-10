from flask import Flask, render_template, request

app = Flask(__name__)
@app.route('/')
def signup_page():
    return render_template('signup.html')



@app.route('/signup', methods=['POST'])

def signup():
        username = request.form['username']
        useremail = request.form['email']

        if not username or not useremail:
            return render_template('signup_failure.html', error='Both username and email required.')
        
        return render_template('signup_successful.html')


if __name__ == '__main__':
    app.run(debug=True)