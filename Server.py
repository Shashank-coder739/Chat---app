import socket
import threading

HOST = "127.0.0.1"
PORT = 12346

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((HOST, PORT))
server.listen()

clients = []

print("Server started... Waiting for connections")

def broadcast(message):
    for client in clients:
        client.send(message)

def handle_client(client):
    while True:
        try:
            message = client.recv(1024)
            print(message.decode())
            broadcast(message)
        except:
            clients.remove(client)
            client.close()
            break

def receive_connections():
    while True:
        client, address = server.accept()
        print(f"Connected: {address}")
        clients.append(client)

        thread = threading.Thread(target=handle_client, args=(client,))
        thread.start()

receive_connections()