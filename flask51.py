from flask import Flask, render_template, request, redirect

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        username = request.form['username']
        age = request.form['age']
        email = request.form['email']

        if not (username and age and email):
            return render_template('signup.html', error='All fields are required.')

        collected_info = {'username': username, 'age': age, 'email': email}
        return render_template('success.html', collected_info=collected_info)

    return render_template('signup.html', error=None)

if __name__ == '__main__':
    app.run(debug=True)
