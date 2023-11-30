from flask import Flask, render_template, request, redirect, flash

app = Flask(__name__)
app.secret_key = 'your_secret_key' 

@app.route('/', methods=['GET', 'POST'])
def sign_up():
    if request.method == 'POST':
        username = request.form.get('username')
        email = request.form.get('email')

        if not username or not email:
            flash('Both username and email are required.', 'error')
        else:
            flash(f'Successfully signned in!  Username: {username},  Email: {email}', 'success')
            return redirect('/')

    return render_template('sign_up.html')

if __name__ == '__main__':
    app.run(debug=True)