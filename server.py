import socket
import sys
import time


s = socket.socket()
host = input(str("Please enter hostname:"))
port = 1234
try:
    s.connect((host, port))
    print("Connected to server")
except:
    print("Connection Failed")

while 1:
    incomming_message = s.recv(1024)
    incomming_message = incomming_message.decode()
    print("Server:>>", incomming_message)
    message = input(str("You:>>"))
    message = message.encode()
    s.send(message)
