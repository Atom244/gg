import socket
import threading

SERVER_IP = input("server ip: ")
PORT = 5555
nickname = input("your nick: ")
# напиши ip который дал хостер (см в инструкции serv.py)
# подключайся

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((SERVER_IP, PORT))

print("connected! write messages\n")

def receive():
    while True:
        try:
            message = client.recv(1024).decode("utf-8")
            print(message)
        except:
            print("connection lost")
            break

threading.Thread(target=receive, daemon=True).start()

while True:
    text = input()
    if text.lower() == "exit":
        client.close()
        break
    message = f"{nickname}: {text}"
    client.send(message.encode("utf-8"))
