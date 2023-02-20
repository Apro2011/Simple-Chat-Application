import socket
import sys
import time


s = socket.socket()
host = socket.gethostname()
print("Server will start on: ", host)
port = 1234
s.bind((host, port))
print("Server is bound successfully")
s.listen(1)
conn, add = s.accept()
print(add, "has connected")
while 1:
    message = input(str("You:>>"))
    message = message.encode()
    conn.send(message)
    incomming_message = conn.recv(1024)
    incomming_message = incomming_message.decode()
    print("Client Message:>>", incomming_message)