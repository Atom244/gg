import socket
import threading

HOST = "0.0.0.0"   
PORT = 5555
# если хост, то нужен просто запуск скрипта
# пропиши ipconfig в терминале и передай собеседнику
# основной ip

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((HOST, PORT))
server.listen()

clients = []

print(f"server running on port {PORT}")

def broadcast(message, sender):
    for client in clients:
        if client != sender:
            try:
                client.send(message)
            except:
                clients.remove(client)

def handle_client(client):
    while True:
        try:
            message = client.recv(1024)
            if not message:
                break
            broadcast(message, client)
        except:
            break

    clients.remove(client)
    client.close()
    print("client disconnected")

while True:
    client, addr = server.accept()
    clients.append(client)
    print(f"connected {addr}")
    threading.Thread(target=handle_client, args=(client,), daemon=True).start()
