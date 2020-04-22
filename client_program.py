# CLIENT CODE
import socket

# not passing any parameters as a socket is already created
client = socket.socket()

# gethostbyname - gets the ip address
import sys

#ip = socket.gethostbyname(socket.gethostname())
ip = sys.argv[1]
port = 1234
client.connect((ip,port))

data = ''
while data != 'Goodbye':
    msg = input("Enter your message to the server: ")
    client.send(msg.encode('utf-8'))
    data = client.recv(1024).decode('utf-8')
    print(data)
