import socket
import time

ClientMultiSocket = socket.socket()
host = '127.0.0.1'
port = 2004

try:
    ClientMultiSocket.connect((host, port))
except socket.error as e:
    print(str(e))

def catch_mess():
    res = ClientMultiSocket.recv(1024)
    print(res.decode('utf-8'))

def send_mess(mess):
    mess = input()
    ClientMultiSocket.send(str.encode(mess))

while True:
    catch_mess()
    send_mess()



#ClientMultiSocket.close()