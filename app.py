# simple web app interface constructor
import os
from dotenv import load_dotenv
from flask import Flask, render_template, session, abort
from flask_socketio import SocketIO
from flask_socketio import emit
from account_utilities import signup_blueprint, login_blueprint, logout_blueprint
from datetime import datetime

app = Flask(__name__)
app.register_blueprint(signup_blueprint)
app.register_blueprint(login_blueprint)
app.register_blueprint(logout_blueprint)

socketio = SocketIO(app)
load_dotenv()

chat_port = os.getenv('CHAT_SERVER_PORT')
chat_port = int(chat_port) if chat_port else 5001
secret_key = os.getenv('SECRET_KEY')
app.secret_key = secret_key

@app.route('/')
def home():
    return render_template('index.html')

# Utility function to check if a user is logged in
def is_logged_in():
    return session.get('username', None)


@socketio.on('send_message')
def handle_send_message_event(data):
    session_user = data.get('username')
    raw_post_time = datetime.now()
    formatted_time = raw_post_time.strftime("%H:%M:%S %Z - %b %d, %Y ")
    if not session_user:
        abort(401)

    data['text'] = f"{data['text']}<br>&nbsp;&nbsp;&nbsp;{session_user}, {formatted_time}"
    emit('receive_message', data, broadcast=True)


if __name__ == '__main__':
    socketio.run(app, host='0.0.0.0', port=chat_port)
