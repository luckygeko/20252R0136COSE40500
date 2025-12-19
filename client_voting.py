import socket

HOST = "127.0.0.1"
PORT = 50000 


client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((HOST, PORT))

print("Connected to voting server.")
print("Commands:")
print("  VOTE A   or   VOTE B   or   VOTE C")
print("  RESULT")
print("  QUIT")

while True:
    msg = input("> ").strip()
    if not msg:
        continue

    client.sendall(msg.encode())

    data = client.recv(1024)
    if not data:
        print("Server closed the connection.")
        break

    print(data.decode().strip())

    if msg.upper().startswith("QUIT"):
         break
    
client.close()
