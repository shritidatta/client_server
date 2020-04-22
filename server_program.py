#TEST SERVER CODE
import socket

#SERVER CODE
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# translates the ipv4  of the host in string format
hostname = socket.gethostname()
print("hostname:", hostname)

# gets the name of the machine
ip = socket.gethostbyname(hostname)

print("ip:", ip)
# same pc
port = 1234
# bind is connect same as connect. so the port taht is created
# port is binded to it
server.bind((ip, port))
server.listen(1) # 1 - indicates 1 client connect
print('Started listening at: ', ip, port)
client, addr = server.accept() 
#server.accept -
#client is the socket object
# addr = is addres of the client

print('Connection set up with:', addr)

while True:
    # data in binary offset format so has to be decoded
    # client will recieve data in size of 1024bytes (buffer size)
    data = client.recv(1024).decode('utf-8')
    if data == 'Hello server':
        client.send('Hello Client'.encode('utf-8'))
    else:
        if data == 'disconnect':
            client.send('Goodbye'.encode('utf-8'))
            client.close()
            break
        else:
            print("received:", data)
            client.send('OK'.encode('utf-8'))
server.close()                
            
