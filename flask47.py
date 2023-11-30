from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return 'Yo whats up, welcome to my flask website!'

@app.route('/user/<username>')
def show_user_profile(username):
    return render_template('profile.html', username=username)

if __name__ == '__main__':
    app.run(debug=True)