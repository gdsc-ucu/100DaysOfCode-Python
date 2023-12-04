from flask import Flask, render_template

app = Flask(__name__)


@app.route('/profile/<username>')
def profile(username):
    user = userdata(username)
    return render_template('nov-day47.html', user=user)

if __name__ == 'main':
    app.run(debug=True)