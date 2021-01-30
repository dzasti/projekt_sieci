import socket
import os
import re
import random
import threading 
import numpy as np
import time
import separate_client
import info_client
import choiceList
import order_
import start_message
import round_
import send_round_mess
import boards
import s_r_mess
#################################### OPENING SERVER SOCKET #######################################

ServerSideSocket = socket.socket()
host = '127.0.0.1'
port = 2004
ThreadCount = [1,2,3,4]
threads = []
blank_list = []

try:
    ServerSideSocket.bind((host, port))
except socket.error as e:
    print(str(e))

ServerSideSocket.listen(4)
s_r_mess.create_file()

###################################### CONNECT AND LOG IN ####################################

all_client_info = info_client.info_client(blank_list)

for x in range(0,4):
    (connection, (ip,port)) = ServerSideSocket.accept()
    newthread = separate_client.separete_client(ip,port,connection,all_client_info)
    newthread.start() 
    threads.append(newthread)
    newthread.join()

################################## FUNCTIONS AND VARIABLES ###################################


choice_list = choiceList.choiceList()
choice_list2 = choiceList.choiceList()

HEADER = 64
FORMAT = 'utf-8'
threadID = 0
threadName = "thread1"
order3 = [0,0,0,0]
orientation = [0,90,180,270]
avialableDomin = list(range(1,49))
cordinate = list(range(-100,101))
VALUE = 200
client_board = [[0 for i in range(VALUE)] for j in range(VALUE)]

def manage_domin():
    global avialableDomin
    global choice_list
    global choice_list2
    for x in range(0,4):
        random_num = random.choice(avialableDomin)
        choice_list.change_list(random_num)
        avialableDomin.remove(random_num)
    choice_list.sort_()
    iterable = choice_list.get_list()
    choice_list2.ch_list = []
    for i in iterable:
        choice_list2.change_list(i)
    choice_list.change_to_string()

def ord2_to_ord1():
    global order
    global order3
    var7 = order3.get()
    order = order_.order_(var7)
    order.change_to_string2()
    
def ord2_to_ord():
    global order
    global order3
    order = order3

def choiceList_type_change():
    global choice_list
    global choice_list2
    choice_list.change_to_list()
    choice_list2.change_to_strlist()

############################################ START MESSAGE ###########################################

temporary_order = np.random.permutation([1,2,3,4])
blank_list2 = [0,0,0,0]


temporary_order = [" ".join(item) for item in temporary_order.astype(str)]

order = order_.order_(temporary_order)
order.change_to_string()
order3 = order_.order_(blank_list2)
manage_domin()

start_mess = all_client_info.get_list()

for x in start_mess:
    s_r_mess.send_m('START ' + str(x[1]) + " " + str(order.get()) + " " + str(choice_list.get_list()) + "\n", x[2])

choiceList_type_change()

newthread = start_message.start_message(order.get(), order3.get(), all_client_info.get_list(),choice_list.get_list(),choice_list2.get_list())
newthread.execute()
print(all_client_info.get_list())

########################################### ROUNDS ####################################################

print("siema")
print(order.get())
print(order3.get())
fuj = 0
ord2_to_ord1()
order3 = order_.order_([0,0,0,0])
#order.orrd = list(order.orrd.split(" "))
board = boards.boards()
board.manage_boards()
while fuj != 11:

    print("siema2")
    print(order.get())
    print(order3.get())

    manage_domin()

    t = send_round_mess.send_round_mess(threadID,threadName,all_client_info.get_list(),choice_list.get_list())
    t.start() 
    threads.append(t)
    t.join() 

    choiceList_type_change()

    t = round_.round_(order.get(), order3.get(), all_client_info.get_list(), choice_list.get_list(), choice_list2.get_list(),board)
    t.execute_()
    varrr = order3.get()
    order = order_.order_(varrr)
    order.change_to_string2()
    order3 = order_.order_([0,0,0,0])
    fuj = fuj + 1
    print(all_client_info.get_list())  


ServerSideSocket.close()
