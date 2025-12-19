import socket

HOST = "127.0.0.1" # local host IP
PORT = 9549 # port number

# generate server socket to connect
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# bind socket with host and port number
server.bind((HOST, PORT))

# server socket listens and waits for connection request
server.listen(5)
print(f"Listening ...")

while True:
    # accept the socket and address tyring to connect
    communication_socket, address = server.accept()

    # receive and store it as name
    name = communication_socket.recv(1).decode()
    print(f"Connected to: {address} , {name}\n")

    # receive and store it as message
    message = communication_socket.recv(1024).decode()
    print(f"Message from client is : {message}")

    # close the TCP connection
    communication_socket.close()
    print(f"Connection with {address} , {name} ended!\n")


