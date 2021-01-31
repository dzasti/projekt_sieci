import socket
import random
import mess_managment
import table

ClientMultiSocket = socket.socket()
host = '127.0.0.1'
port = 2004
HEADER = 64
FORMAT = 'utf-8'
upper = 0
lower = 0
guard = 0
stage = 0
domins = []

try:
    ClientMultiSocket.connect((host, port))
except socket.error as e:
    print(str(e))

table = table.table([])
recv_pocket = mess_managment.gettig_mess(1,"rcv_pck",ClientMultiSocket,table)
recv_pocket.start()

def login_mess(connection):
    random_number = random.randint(100000, 999999)
    random_number = str(random_number)
    m = "LOGIN " + random_number + "\n"
    connection.send(str.encode(m))
    print(m,end = "")

def start_mess(connection,res):
    global domins
    res = res.replace('START ', '')
    res = res.rstrip("\n")
    res = list(res.split(" "))
    res = res[5:]
    domins = res
    print(domins)

def round_(connection,res):
    global domins
    res = res.replace('ROUND ', '')
    res = res.rstrip("\n")
    res = list(res.split(" "))
    domins =res
    print(domins)

def choice(connection):
    global domins
    domin = random.choice(domins)
    m = "CHOOSE " + str(domin) + "\n"
    connection.send(str.encode(m))
    print(m, end = "")


def move(connection):
    global upper
    global lower
    arr = [upper,lower]
    line = random.choice(arr)
    if(line == upper):
        line = line + 1
        upper = upper + 1
    else:
        line = line - 1
        lower = lower - 1
    m = "MOVE " + str(line) + " 0" + " 0\n"
    connection.send(str.encode(m))
    print(m, end = "")

while True:

    if table.get(): 
        mess = table.get_1_el()
        table.remove()
        print(mess)
        if "ERROR" in mess:
            print("heeeee")
            if stage == 1:
                print("ko")
                choice(ClientMultiSocket)
            else:
                print("mo")
                move(ClientMultiSocket)
        if "CONNECT" in mess:
            login_mess(ClientMultiSocket)
        elif "START" in mess:
            start_mess(ClientMultiSocket,mess)
        elif "YOUR CHOICE" in mess:
            stage = 1
            choice(ClientMultiSocket)
        elif "YOUR MOVE" in mess:
            stage = 2
            move(ClientMultiSocket)
        elif "ROUND" in mess:
            round_(ClientMultiSocket,mess)
       
