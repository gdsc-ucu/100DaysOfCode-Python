from flask import Flask, render_template, request, redirect, url_for, flash
from flask_socketio import SocketIO, emit, join_room, leave_room
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import LoginManager, UserMixin, login_user, login_required, logout_user, current_user
from datetime import datetime

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'  # SQLite database file
db = SQLAlchemy(app)
socketio = SocketIO(app)
login_manager = LoginManager(app)
connected_users = {}

# User model
class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password = db.Column(db.String(120), nullable=False)

# Message model
class Message(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.String(500), nullable=False)
    sender = db.Column(db.String(80), nullable=False)
    timestamp = db.Column(db.DateTime, default=datetime.utcnow)

# Private message model
class PrivateMessage(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.String(500), nullable=False)
    sender = db.Column(db.String(80), nullable=False)
    recipient = db.Column(db.String(80), nullable=False)
    timestamp = db.Column(db.DateTime, default=datetime.utcnow)

# Create database tables
with app.app_context():
    db.create_all()

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

@app.route('/', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')

        user = User.query.filter_by(username=username).first()
        if user and check_password_hash(user.password, password):
            login_user(user)
            flash(f'Logged in as {username}', 'success')

            # Emit stored messages to the new user
            messages = Message.query.order_by(Message.timestamp).all()
            print("Stored Messages:", messages)  # Check if messages are retrieved
            for message in messages:
                print("Emitting Message:", message.content)  # Check if each message is emitted
                socketio.emit('message', {'message': message.content, 'sender': message.sender}, room=current_user.username)

            return redirect(url_for('index'))
        else:
            flash('Invalid username or password', 'error')

    return render_template('login.html')
   

@app.route('/index')
@login_required
def index():
    return render_template('chat.html', username=current_user.username)

@app.route('/register', methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('index'))

    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')

        if not username or not password:
            flash('Please enter both username and password', 'error')
        else:
            if User.query.filter_by(username=username).first():
                flash('Username already exists. Choose a different one', 'error')
            else:
                hashed_password = generate_password_hash(password, method='pbkdf2:sha256', salt_length=8)
                new_user = User(username=username, password=hashed_password)
                db.session.add(new_user)
                db.session.commit()

                login_user(new_user)
                flash(f'Account created for {username}. You are now logged in', 'success')
                return redirect(url_for('index'))

    return render_template('register.html')

@app.route('/logout')
@login_required
def logout():
    logout_user()
    flash('Logged out successfully', 'success')
    return redirect(url_for('login'))  # Update 'register' to 'login'



@socketio.on('message')
@login_required
def handle_message(msg):
    full_msg = f"{current_user.username}: {msg}"
    print('Received message:', full_msg)

    # Save the message to the database
    new_message = Message(content=full_msg, sender=current_user.username)
    db.session.add(new_message)
    db.session.commit()

    socketio.emit('message', {'message': full_msg, 'sender': current_user.username})

@socketio.on('connect')
@login_required
def handle_connect():
    join_room(current_user.username)

    # Emit stored messages to the connected user
    messages = Message.query.order_by(Message.timestamp).all()
    for message in messages:
        socketio.emit('message', {'message': message.content, 'sender': message.sender}, room=current_user.username)

    # Emit stored private messages to the connected user
    sender_username = current_user.username
    stored_private_messages = PrivateMessage.query.filter_by(sender=sender_username).order_by(PrivateMessage.timestamp).all()
    for private_message in stored_private_messages:
        recipient = private_message.recipient
        message_content = private_message.content
        socketio.emit('message', {'message': f"[Private] {sender_username} to {recipient}: {message_content}", 'sender': 'System'}, room=recipient)

    emit('message', {'message': f"{current_user.username} has joined the chat.", 'sender': 'System'}, room=current_user.username)
    # Debugging print statements
    print('Stored Messages:', messages)
    print('Stored Private Messages:', stored_private_messages)

@socketio.on('disconnect')
@login_required
def handle_disconnect():
    leave_room(current_user.username)
    socketio.emit('message', f"{current_user.username} has left the chat.", room=current_user.username)


@socketio.on('private_message')
@login_required
def handle_private_message(data):
    recipient = data['recipient']
    message_content = data['message']
    sender_username = current_user.username

    # Save the private message to the database
    new_private_message = PrivateMessage(
        content=message_content,
        sender=sender_username,
        recipient=recipient
    )
    db.session.add(new_private_message)
    db.session.commit()

    # Emit the private message to the sender
    emit('message', {'message': f"[Private] {sender_username} to {recipient}: {message_content}", 'sender': 'System'}, room=sender_username)

    # Emit the private message to the recipient if they are currently connected
    if recipient in connected_users:
        recipient_sid = connected_users[recipient]
        # Use the socketio object associated with the recipient's room
        socketio.emit('message', {'message': f"[Private] {sender_username} to {recipient}: {message_content}", 'sender': 'System'}, room=recipient_sid)
    else:
        # Recipient not connected, you could handle this case differently, e.g., send a notification
        print(f"Recipient {recipient} not currently connected. Saving the message for later.")

if __name__ == '__main__':
    socketio.run(app, debug=True)
