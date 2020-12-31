import socket
import os
from _thread import *
import re
import random
import threading 
import numpy as np

#################################### OPENING SERVER SOCKET #######################################

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

###################################### CONNECT AND LOG IN ########################################

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

################################## FUNCTIONS AND FUTURE VARIABLES ###################################

avialableDomin = list(range(1,49))
choiceList = []
choiceList2 = []
order = []
order3 = [0,0,0,0]
orientation = [0,90,180,270]
cordinate = list(range(-100,101))


def manage_domin():
    global avialableDomin
    global choiceList
    global choiceList2
    for x in range(0,4):
        random_num = random.choice(avialableDomin)
        choiceList.append(random_num)
        avialableDomin.remove(random_num)
    choiceList.sort()
    choiceList2 = choiceList
    #choiceLst2 = map(str, choiceList2)
    choiceList = map(str, choiceList)
    choiceList = ' '.join(choiceList)

def ord2_to_ord1():
    global order
    global order3
    global order2
    order = order3
    order = [str(i) for i in order]
    order2 = ' '.join(order)

############################################ START MESSAGE ###########################################

order = np.random.permutation([1,2,3,4])
y = 0

order = [",".join(item) for item in order.astype(str)]
order2 = ' '.join(order)

for x in listOfIndexes:
    x[1] = order[y]
    y = y + 1

manage_domin()
print(type(choiceList[0]))

for x in listOfIndexes:
    x[2].send(str.encode('START ' + x[1] + " " + order2  + " " + choiceList))

choiceList = list(choiceList.split(" "))

for x in order:
    for x2 in listOfIndexes:
        if x2[1] == x:
            x3 = x2
    x3[2].send(str.encode("YOUR CHOICE"))
    while True:
        data = x3[2].recv(2048)
        response = data.decode('utf-8')
        regex = re.compile('CHOOSE *')
        match = 'no'
        print("odebralo komunikat")
        for string in choiceList:
            if response.replace('CHOOSE ', '') == string:
                match = 'yes'
                print("znalazlo element")
        if re.match(regex, response) and match == 'yes':
            print("weszlo do petli")
            x3[2].send(str.encode("OK"))
            print(choiceList2)
            print(type(response.replace('CHOOSE ', '')))
            print(type(choiceList2[0]))
            choiceList2 = list(map(str, choiceList2))
            print(type(choiceList2[0]))
            order3[choiceList2.index(response.replace('CHOOSE ', ''))] = x3[1]
            print(order3)
            choiceList.remove(response.replace('CHOOSE ', ''))
            for x4 in listOfIndexes:
                if x4 != x3:
                    x4[2].send(str.encode("PLAYER CHOICE " + x3[1] + " " + response.replace('CHOOSE ', '')))
            break
        else:
            x3[2].send(str.encode("ERROR"))

print(order3)

########################################### ROUNDS ####################################################

ord2_to_ord1()
manage_domin()
for x in listOfIndexes:
    x[2].send(str.encode("ROUND " + choiceList + " " + order2))
choiceList = list(choiceList.split(" "))

for x in order:
    for x2 in listOfIndexes:
        if x2[1] == x:
            x3 = x2
    x3[2].send(str.encode("YOUR MOVE"))

    while True:
        data = x3[2].recv(2048)
        response = data.decode('utf-8')
        regex = re.compile('MOVE *')
        match = 'no'
        print("odebralo komunikat")
        helpList = list(response.split(" "))
        if re.match(regex, response) and (int(helpList[1]) in cordinate) and (int(helpList[2]) in cordinate) and (int(helpList[3]) in orientation) and len(helpList) == 4:
            print("weszlo do petli")
            x3[2].send(str.encode("OK"))
            for x4 in listOfIndexes:
                if x4 != x3:
                    x4[2].send(str.encode("PLAYER MOVE " + helpList[1] + " " + helpList[2] + " " + helpList[3] + " "))
            break
        else:
            x3[2].send(str.encode("ERROR"))
    
    x3[2].send(str.encode("YOUR CHOICE"))
    while True:
        data = x3[2].recv(2048)
        response = data.decode('utf-8')
        regex = re.compile('CHOOSE *')
        match = 'no'
        print("odebralo komunikat")
        for string in choiceList:
            if response.replace('CHOOSE ', '') == string:
                match = 'yes'
                print("znalazlo element")
        if re.match(regex, response) and match == 'yes':
            print("weszlo do petli")
            x3[2].send(str.encode("OK"))
            choiceList2 = list(map(str, choiceList2))
            order3[choiceList2.index(response.replace('CHOOSE ', ''))] = x3[1]
            choiceList.remove(response.replace('CHOOSE ', ''))
            for x4 in listOfIndexes:
                if x4 != x3:
                    x4[2].send(str.encode("PLAYER CHOICE " + x3[1] + " " + response.replace('CHOOSE ', '')))
            break
        else:
            x3[2].send(str.encode("ERROR"))


ServerSideSocket.close()
