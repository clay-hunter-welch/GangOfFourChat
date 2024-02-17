import socket
#import threading
from dotenv import load_dotenv
import os
#from message import *

load_dotenv()

chat_port = os.getenv('CHAT_SERVER_PORT')
chat_port = int(chat_port) if chat_port else 5001

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(('localhost', chat_port))