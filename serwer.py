import socket
import os
from _thread import *
import re
import random

ServerSideSocket = socket.socket()
host = '127.0.0.1'
port = 2004
ThreadCount = 0
listOfIndexes = []
#listOfClients = []
order = []
threads = []

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
            global ThreadCount
            ThreadCount = ThreadCount + 1
            listOfIndexes.append([response,ThreadCount,connection])
            #print('Thread Number: ' + str(ThreadCount))
            break
        else:
            connection.send(str.encode('ERROR')) 

for x in range(0,4):
    Client, address = ServerSideSocket.accept()
    t = start_new_thread(multi_threaded_client, (Client, ))
	thread.append(t)
    #listOfClients.append(Client)

for x in threads:
	x.join()

#random.shuffle(ListOfIndexes[])

order = np.random.permutation([1,2,3,4])
y = 0

for x in ListOfIndexes:
    x[1] = order[y]
    y = y + 1

for x in ListOfIndexes:
    x[2].send(str.encode('START ' + x[1] + " " + order ))

ServerSideSocket.close()
