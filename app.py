# simple web app interface constructor
import os
from dotenv import load_dotenv
from flask import Flask, render_template
from flask_socketio import SocketIO
from flask_socketio import emit

app = Flask(__name__)
socketio = SocketIO(app)
load_dotenv()

chat_port = os.getenv('CHAT_SERVER_PORT')
chat_port = int(chat_port) if chat_port else 5001

@app.route('/')
def home():
    return render_template('index.html')


@socketio.on('send_message')
def handle_send_message_event(data):
    print('Message received:', data['text'])
    emit('receive_message', data, broadcast=True)


if __name__ == '__main__':
    socketio.run(app, host='0.0.0.0', port=chat_port)
