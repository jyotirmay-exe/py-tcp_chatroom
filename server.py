import socket
import threading
import json
from datetime import datetime

addr = {}
with open('configs/svr-config.json','r') as f:
    addr = json.load(f)

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((addr['ip'],addr['port']))
server.listen()
ip = addr['ip']
port = addr['port']
print(f'Listening to {ip}:{port}')

admin = None

clients = []
nicknames = []

def broadcast(mssg):
    with open("configs/chat-log.txt",'a') as log:
        log.write(f'[{datetime.now().strftime("%d/%m/%y %T")}] {mssg}\n')
    for cl in clients:
        cl.send(mssg.encode('ascii'))

def listen(cl):
    while True:
        try:
            msg = cl.recv(1024).decode('ascii')
            broadcast(msg)
        except:
            nick = nicknames[clients.index(cl)]
            clients.remove(cl)
            print(f'{nick} disconnected.')
            cl.close()
            nicknames.remove(nick)
            broadcast(f'{nick} left the chat!')
            break
def accept():
    while True:
        client,addr = server.accept()
        print(str(addr),'connected as',end = ' ')
        nick = client.recv(1024).decode('ascii')
        print(nick)
        nicknames.append(nick)
        clients.append(client)
        broadcast(f'{nick} joined the chat!')
        thread = threading.Thread(target=listen,args=(client,))
        thread.start()

accept()