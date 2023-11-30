from flask import Flask, render_template

app = Flask(__name__)

# Sample user data
users = {
    "peter_kure":{"name":"Peter Kure","email":"peter@example.com"},
    "allan_smith":{"name":"Allan Smith","email":"allan@example.com"},
    "captain_alex": {"name": "Captain Alex", "email": "captain@example.com"},
    "jorja_smith": {"name": "Jorga Smith", "email": "jorja@example.com"}
}

@app.route('/profile/<username>')
def show_profile(username):
    user = users.get(username, None)
    if user:
        return render_template('profile.html', user=user)
    else:
        return "User not found", 404

if __name__ == '__main__':
    app.run(debug=True)
