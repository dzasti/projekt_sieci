import socket
import os
from _thread import *
import re
import random
import threading 
import numpy as np

ServerSideSocket = socket.socket()
host = '127.0.0.1'
port = 2004
ThreadCount = 0
listOfIndexes = []
threads = []

try:
    ServerSideSocket.bind((host, port))
except socket.error as e:
    print(str(e))

ServerSideSocket.listen(4)

class separete_client(threading.Thread):

    def __init__(self, threadID, name):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.name = name

    def run(self):
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
                break
            else:
                connection.send(str.encode('ERROR')) 

for x in range(0,4):
    (connection, (ip,port)) = ServerSideSocket.accept()
    newthread = separete_client(ip,port)
    newthread.start() 
    threads.append(newthread)

for t in threads: 
    t.join() 

##########################################   END OF LOGIN  ##########################################

################################## functions and future variables ###################################
avialableDomin = list(range(1,49))
choiceList = []

def manage_domin():
    global avialableDomin
    global choiceList
    choiceList.clear()
    for x in range(0,4):
        random_num = random.choice(avialableDomin)
        choiceList.append(random_num)
        avialableDomin.remove(random_num)
    choiceList = map(str, choiceList)
    choiceList = ' '.join(choiceList)

############################################ START MESSAGE ###########################################

order = []
order = np.random.permutation([1,2,3,4])
y = 0

order = [",".join(item) for item in order.astype(str)]
order2 = ' '.join(order)

for x in listOfIndexes:
    x[1] = order[y]
    y = y + 1

manage_domin()

for x in listOfIndexes:
    x[2].send(str.encode('START ' + x[1] + " " + order2  + " " + choiceList))


########################################### END OF START ############################################


ServerSideSocket.close()
