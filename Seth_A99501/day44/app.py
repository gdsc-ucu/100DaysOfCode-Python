from flask import Flask, render_template
app=Flask(__name__)

@app.route("/")
def home():
    return "Hello FlaskI hope I got you"

@app.route("/about")
def about():
    return render_template('about.html')

if __name__=="__main__":
    app.debug=True