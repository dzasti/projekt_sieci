import socket
import random

ClientMultiSocket = socket.socket()
host = '127.0.0.1'
port = 2004
HEADER = 64
FORMAT = 'utf-8'
upper = 0
lower = 0

try:
    ClientMultiSocket.connect((host, port))
except socket.error as e:
    print(str(e))

def geneate_ran_num(arr):
    random_num = random.choice(arr)
    return random_num

def generate_ran_move(upper1,lower1):
    global upper
    global lower
    arr = [upper1,lower1]
    line = random.choice(arr)
    if(line == upper1):
        line = line + 1
        upper = upper + 1
    else:
        line = line - 1
        lower = lower - 1
    return "MOVE " + str(line) + " 0" + " 0\n"

def send_m(mess,connection):
    message = mess.encode(FORMAT)
    mess_length = len(mess)
    send_length = str(mess_length).encode(FORMAT)
    send_length += b' ' * (HEADER - len(send_length))
    connection.send(send_length)
    connection.send(message)

def recv_mess(connection):
     msg_length = connection.recv(HEADER).decode(FORMAT)
     msg_length = int(msg_length)
     msg = connection.recv(msg_length).decode(FORMAT)
     return msg

res = recv_mess(ClientMultiSocket) 
print(res, end = '')

######################################## LOGGING IN ##########################################

while res != "OK\n":
    random_number = random.randint(100000, 999999)
    random_number = str(random_number)
    m = "LOGIN " + random_number + "\n"
    print(m, end = "")
    send_m(m,ClientMultiSocket)
    res = res = recv_mess(ClientMultiSocket)
    print(res, end = '')

######################################## START ###############################################

res = recv_mess(ClientMultiSocket)
print(res, end = "")
res = res.replace('START ', '')
order = [res[2], res[4], res[6] ,res[8]]
check = res[0]
res = res.rstrip("\n")
res = list(res.split(" "))
res = res[5:]
domins = res
wart = 0
print(domins) 
print(order[wart], check)
while order[wart] != check:
    res = recv_mess(ClientMultiSocket)
    print(res, end = "")
    wart = wart + 1
res = recv_mess(ClientMultiSocket)
print(res, end = "")
while res != "OK\n":
    Input = "CHOOSE " + str(geneate_ran_num(domins)) + "\n"
    send_m(Input,ClientMultiSocket)
    print(Input, end="")
    res = recv_mess(ClientMultiSocket)
    print(res, end = "")
Input = Input.rstrip("\n")
taken_domin = domins.index(Input.replace('CHOOSE ', ''))
while wart != 3:
    res = recv_mess(ClientMultiSocket)
    print(res, end = "")
    wart = wart + 1

print("koniec startu")

####################################### ROUNDS ################################################
fuj = 0

while fuj != 11:
    res = recv_mess(ClientMultiSocket)
    print(res, end = "")
    res = res.replace('ROUND ', '')
    res = res.rstrip("\n")
    res = list(res.split(" "))
    domins2 =res
    print(domins2)
    print(taken_domin)
    wart = 0
    while wart != taken_domin:
        res = recv_mess(ClientMultiSocket)
        print(res, end = "")
        res = recv_mess(ClientMultiSocket)
        print(res, end = "")
        wart = wart + 1
    res = recv_mess(ClientMultiSocket)
    print(res,end = "")
    while res != "OK\n":
        Input = generate_ran_move(upper,lower)
        send_m((Input),ClientMultiSocket)
        print(Input, end = "")
        res = recv_mess(ClientMultiSocket)
        print(res,end = "")
    res = recv_mess(ClientMultiSocket)
    print(res,end = "")
    while res != "OK\n":
        Input = "CHOOSE " + str(geneate_ran_num(domins2)) + "\n"
        send_m(Input,ClientMultiSocket)
        print(Input, end="")
        res = recv_mess(ClientMultiSocket)
        print(res, end = "")
    Input = Input.rstrip("\n")
    taken_domin = domins2.index(Input.replace('CHOOSE ', ''))
    while wart != 3:
        res = recv_mess(ClientMultiSocket)
        print(res,end = "")
        res = recv_mess(ClientMultiSocket)
        print(res,end = "")
        wart = wart + 1
    fuj = fuj + 1

ClientMultiSocket.close()
