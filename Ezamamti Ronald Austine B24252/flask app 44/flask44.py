from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return 'Yo whats up, welcome to my website!'

@app.route('/about')
def about():
    return render_template('about.html', title='Home')

if __name__ == '__main__':
    app.run(debug=True)