import socket
import threading
import json
import sys

nickname = None

fail = False

addr = {}
with open('configs/cl-config.json','r') as f:
    addr = json.load(f)

client = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
client.connect((addr['ip'],addr['port']))

def nick():
    global nickname
    nickname = input('Enter your nickname to be shown to all : ')
    client.send(nickname.encode('ascii'))

def rec():
    try:
        while True:
            print(client.recv(1024).decode('ascii'))
    except ConnectionResetError as ex:
        print('Server stopped listening to the specified address. Press enter to exit...')
        global fail
        fail == True
        sys.exit()


def send():
    global fail
    global nickname
    while True:
        mssg = input("")
        try:
            client.send(f"{mssg}".encode('ascii'))
        except:
            sys.exit()

nick()

sender = threading.Thread(target=send)
sender.start()

recver = threading.Thread(target=rec)
recver.start()