from flask import Flask, render_template, request, redirect, url_for, session, flash
from flask_socketio import SocketIO, emit
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'  # SQLite database file
db = SQLAlchemy(app)
socketio = SocketIO(app)

# User model
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password = db.Column(db.String(120), nullable=False)

# Create database tables
with app.app_context():
    db.create_all()

@app.route('/', methods=['GET', 'POST'])
def login():
    if 'username' in session:
        return redirect(url_for('index'))
    
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')

        user = User.query.filter_by(username=username).first()
        if user and check_password_hash(user.password, password):
            session['username'] = user.username
            return redirect(url_for('index'))
        else:
            flash('Invalid username or password', 'error')

    return render_template('login.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
    if 'username' in session:
        return redirect(url_for('index'))
    
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')

        if not username or not password:
            flash('Please enter username and password', 'error')
        else:
            if User.query.filter_by(username=username).first():
                flash('username already exist. choose a different one', 'error')
            else:
                hashed_password = generate_password_hash(password, method='pbkdf2:sha256', salt_length=8)
                new_user = User(username=username, password=hashed_password)
                db.session.add(new_user)
                db.session.commit()

                session['username'] = new_user.username
                return redirect(url_for('index'))
    return render_template('register.html')   

@app.route('/index')
def index():
    if 'username' in session:
        return render_template('chat.html', username=session['username'])
    return redirect(url_for('login'))

@app.route('/logout')
def logout():
    session.pop('username', None)
    return redirect(url_for('login'))

@socketio.on('message')
def handle_message(msg):
    if 'username' in session:
        full_msg = f"{session['username']}: {msg}"
        print('Received message:', full_msg)
        socketio.emit('message', full_msg)

if __name__ == '__main__':
    socketio.run(app, debug=True)
