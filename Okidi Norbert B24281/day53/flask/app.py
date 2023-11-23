from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/user-form/', methods=['GET', 'POST'])

def user_form():
    if request.method == 'POST':
        pass
    print(request.form)
    return render_template('user_form.html')

if __name__ == 'main':
    app.run(debug=True)