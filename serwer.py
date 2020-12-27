import socket
import os
from _thread import *
import re

ServerSideSocket = socket.socket()
host = '127.0.0.1'
port = 2004
ThreadCount = 0
listOfIndexes = []
count = 0
try:
    ServerSideSocket.bind((host, port))
except socket.error as e:
    print(str(e))

ServerSideSocket.listen(4)

def multi_threaded_client(connection):
    connection.send(str.encode('CONNECTED'))
    while True:
        data = connection.recv(2048)
        response = data.decode('utf-8')
        regex = re.compile('LOGIN ......')
        match = 'no'
        for string in listOfIndexes:
            if response == string:
                match = 'yes'
        if re.match(regex, response) and match == 'no':
            connection.send(str.encode('OK'))
            listOfIndexes.append(response)
            global ThreadCount
            ThreadCount = ThreadCount + 1
            #print('Thread Number: ' + str(ThreadCount))
            break
        else:
            connection.send(str.encode('ERROR')) 
    return ThreadCount    
    connection.close()

while count != 4:
    Client, address = ServerSideSocket.accept()
    count = start_new_thread(multi_threaded_client, (Client, ))
    print('Thread Number: ' + str(count))

print("koniec")
ServerSideSocket.close()
