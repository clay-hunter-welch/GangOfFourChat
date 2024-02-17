# Gang of Four project:
# Creational patterns:
# Structural patterns:
# Behavioral patterns:
# Concurrency patterns:

from dotenv import load_dotenv
import os
from server import ServerSingleton

load_dotenv()

server_port = os.getenv('CHAT_SERVER_PORT')
server_port = int(server_port) if server_port else 5001

server = ServerSingleton(server_port)
server.start()
