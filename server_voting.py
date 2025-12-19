import socket
import threading

HOST = "127.0.0.1" 
PORT = 50000 

votes = {"A": 0, "B": 0, "C": 0}
lock = threading.Lock()


def format_results(prefix="Current result: "):
    return f"{prefix}A={votes['A']}, B={votes['B']}, C={votes['C']}\n"


def handle_client(conn, addr):
    print(f"Connected with {addr}")
    with conn:
        while True:
            data = conn.recv(1024)
            if not data:
                break

            msg = data.decode().strip()
            parts = msg.split()
            cmd = parts[0].upper()

            response = ""

            if cmd == "VOTE" and len(parts) >= 2:
                option = parts[1].upper()
                if option in votes:
                    with lock:
                        votes[option] += 1
                    response = format_results(prefix="Thank you for voting. ")
                else:
                    response = "Invalid option. Use: VOTE A or VOTE B or VOTE C\n"

            elif cmd == "RESULT":
                response = format_results()

            elif cmd == "QUIT":
                response = "Bye!\n"
                conn.sendall(response.encode())
                break

            else:
                response = (
                    "Unknown command.\n"
                    "Available commands:\n"
                    "  VOTE A | VOTE B | VOTE C\n"
                    "  RESULT\n"
                    "  QUIT\n"
                )

            conn.sendall(response.encode())

    print(f"Connection closed: {addr}")


server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
server.bind((HOST, PORT))
server.listen()
        
print(f"Listening on {HOST}:{PORT}")

while True:
    conn, addr = server.accept()
    thread = threading.Thread(target=handle_client, args=(conn, addr), daemon=True)
    thread.start()

