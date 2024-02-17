# Gang of Four project:
# Creational patterns:
#   -Singleton
# Structural patterns:
# Behavioral patterns:
# Concurrency patterns:

import socket
import threading


class ServerSingleton:
    _instance = None

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super(ServerSingleton, cls).__new__(cls)
        return cls._instance

    def __init__(self, port):
        if not hasattr(self, 'initialized'):
            self.port = port
            self.socket = None
            self.initialized = True
            self.clients = []

    def setup_server(self):
        # initializes the server socket
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.socket.bind(('localhost', self.port))
        self.socket.listen()
        print(f"Server listening on port {self.port}")

    def accept_connections(self):
        # accepts incoming client connection requests
        print("Server ready to accept connections....")
        while True:
            client_socket, addr = self.socket.accept()
            print(f"Connection from {addr} has been established.")
            self.clients.append(client_socket)
            threading.Thread(target=self.handle_client, args=(client_socket,)).start()

    def handle_client(self):
        # handles comms with a connected client
        try:
            while True:
                message = client_socket.recv(1024)
                if not message:
                    break
                print(f"Received: {message.decode('utf-8')}")
                client_socket.send("Message received".encode('utf-8'))
        finally:
            client_socket.close()

    def start(self):
        # start server
        self.setup_server()
        self.accept_connections()


    # ADD SERVER METHODS HERE: START, STOP
def handle_client(client_socket):
    while True:
        message = client_socket.recv(1024)
        if not message:
            break
        print(f"Received: {message.decode('utf-8')}")
        client_socket.send("Message received".encode('utf-8'))
    client_socket.close()

