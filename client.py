import socket

HOST = "127.0.0.1" # local host IP
PORT = 9549 # port number

# create TCP socket
c = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# connect to the server
c.connect((HOST, PORT))

# your name
name = input("Enter your name: ")

# send your name to the server encoding it into byte
c.send(name.encode())

# send the message encoding it into byte
c.send("Hello World".encode())

# print out what you receive from the server upto 1024 bytes,
# decoding byte into the sentence you can read
print(c.recv(1024).decode())



