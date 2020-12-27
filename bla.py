import socket
import os
from _thread import *

ServerSideSocket = socket.socket()
host = '127.0.0.1'
port = 2004
ThreadCount = 0
try:
    ServerSideSocket.bind((host, port))
except socket.error as e:
    print(str(e))

ServerSideSocket.listen(4)
threadsList = []
threadCount = 0

def multi_threaded_client(connection):
    response = "CONNECTED"
    connection.sendall(str.encode(response))
    #connection.close()

def send_mess(connection, mess):
    connection.sendall(str.encode(mess))

def catch_mess(connection):
    mess = ClientMultiSocket.recv(1024)
    print(mess.decode('utf-8'))

while threadCount != 4:
    Client, address = ServerSideSocket.accept()
    threadslist.append(start_new_thread(multi_threaded_client, (Client, )))




ServerSideSocket.close()