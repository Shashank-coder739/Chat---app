import socket
import threading

# Server IP and port
HOST = "127.0.0.1"  # If on different laptops, replace with server laptop IP
PORT = 12346         # Make sure it matches server.py

# Connect to the server
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((HOST, PORT))

# Ask the user for their name
username = input("Enter your username: ")

# Function to receive messages from server
def receive_messages():
    while True:
        try:
            message = client.recv(1024).decode("utf-8")
            print(message)
        except:
            print("Disconnected from server")
            client.close()
            break

# Function to send messages to server
def send_messages():
    while True:
        message = f"{username}: {input()}"
        client.send(message.encode("utf-8"))

# Start threads for sending and receiving
receive_thread = threading.Thread(target=receive_messages)
receive_thread.start()

send_thread = threading.Thread(target=send_messages)
send_thread.start()