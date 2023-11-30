from flask import Flask, render_template, request
from flask_wtf import FlaskForm
from wtforms import StringField, FileField, SubmitField
from wtforms.validators import InputRequired
import os

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret_key'
app.config['UPLOAD_FOLDER'] = 'uploads' 
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024  

class UserForm(FlaskForm):
    username = StringField('Username', validators=[InputRequired()])
    profile_pictures = FileField('Profile Pictures', validators=[InputRequired()], multiple=True)
    submit = SubmitField('Submit')

@app.route('/user_form', methods=['GET', 'POST'])
def user_form():
    form = UserForm()

    if form.validate_on_submit():
        username = form.username.data

        uploaded_files = []
        for uploaded_file in form.profile_pictures.data:
            filename = os.path.join(app.config['UPLOAD_FOLDER'], uploaded_file.filename)
            uploaded_file.save(filename)
            uploaded_files.append(uploaded_file.filename)

        return render_template('submission_result.html', username=username, uploaded_files=uploaded_files)

    return render_template('user_form_multiple_files.html', form=form)

if __name__ == '__main__':
    app.run(debug=True)
