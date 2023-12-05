from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')

def hello_world():
    return 'Hello World'

@app.route('/about')
def about():
    return render_template('about.html', website_name = 'about', description = 'This my first website.')


if __name__ == '__main__':
    app.run(debug=True)

