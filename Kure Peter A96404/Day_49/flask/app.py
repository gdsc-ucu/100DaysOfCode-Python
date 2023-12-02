from flask import Flask, render_template_string, request, flash, redirect
from flask_wtf import FlaskForm
from wtforms import StringField, validators

app = Flask(__name__)
app.secret_key = 'secret123'  # Set your secret key

class SignupForm(FlaskForm):
    username = StringField('Username', [validators.InputRequired()])
    email = StringField('Email', [validators.Email(), validators.InputRequired()])

@app.route('/signup', methods=['GET', 'POST'])
def signup():
    form = SignupForm()
    if form.validate_on_submit():
        return 'Signup successful!'
    return render_template_string('''
        <form method="POST">
            {{ form.csrf_token }}
            Username: {{ form.username }}<br>
            Email: {{ form.email }}<br>
            <input type="submit" value="Sign Up">
        </form>
    ''', form=form)

if __name__ == '__main__':
    app.run(debug=True)
