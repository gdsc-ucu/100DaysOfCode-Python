from flask import Flask, render_template, request
from flask_wtf import FlaskForm
from wtforms import StringField, FileField

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret_key'

class UserForm(FlaskForm):
    username = StringField('Username')
    profile_pictures = FileField('Profile Pictures', multiple=True)

@app.route('/user_form', methods=['GET', 'POST'])
def user_form():
    form = UserForm()

    if form.validate_on_submit():
        username = form.username.data
        profile_pictures = [file.filename for file in form.profile_pictures.data]

        return f'Hello, {username}! Profile Pictures: {", ".join(profile_pictures)}'

    return render_template('user_form_advanced.html', form=form)

if __name__ == '__main__':
    app.run(debug=True)
