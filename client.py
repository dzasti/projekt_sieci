import socket

ClientMultiSocket = socket.socket()
host = '127.0.0.1'
port = 2004

try:
    ClientMultiSocket.connect((host, port))
except socket.error as e:
    print(str(e))

res = ClientMultiSocket.recv(1024)
print(res.decode('utf-8'), end = '')

######################################## LOGGING IN ##########################################

while res != "OK\n":
    Input = input()
    ClientMultiSocket.send(str.encode(Input + "\n"))
    res = ClientMultiSocket.recv(1024)
    res = res.decode('utf-8')
    print(res, end = '')

######################################## START ###############################################

res = ClientMultiSocket.recv(1024)
res = res.decode('utf-8')
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
    res = ClientMultiSocket.recv(1024)
    res = res.decode('utf-8')
    print(res, end = "")
    wart = wart + 1
res = ClientMultiSocket.recv(1024)
res = res.decode('utf-8')
print(res, end = "")
while res != "OK\n":
    Input = input()
    ClientMultiSocket.send(str.encode(Input + "\n"))
    #print(Input + "\n", end = "")
    res = ClientMultiSocket.recv(1024)
    res = res.decode('utf-8')
    print(res, end = "")
taken_domin = domins.index(Input.replace('CHOOSE ', ''))
while wart != 3:
    res = ClientMultiSocket.recv(1024)
    res = res.decode('utf-8')
    print(res, end = "")
    wart = wart + 1

print("koniec startu")

####################################### ROUNDS ################################################
fuj = 0
HEADER = 64
FORMAT = 'utf-8'

def recv_mess():
     msg_length = ClientMultiSocket.recv(HEADER).decode(FORMAT)
     msg_length = int(msg_length)
     msg = ClientMultiSocket.recv(msg_length).decode(FORMAT)
     print(msg, end = "")


while fuj != 3:
    res = ClientMultiSocket.recv(HEADER).decode(FORMAT)
    res = int(res)
    msg = ClientMultiSocket.recv(res).decode(FORMAT)
    print(msg, end = "")
    res = msg.replace('ROUND ', '')
    res = res.rstrip("\n")
    res = list(res.split(" "))
    domins2 =res
    print(domins2)
    print(taken_domin)
    wart = 0
    while wart != taken_domin:
        res = ClientMultiSocket.recv(1024)
        res = res.decode('utf-8')
        print(res, end = "")
        res = ClientMultiSocket.recv(1024)
        res = res.decode('utf-8')
        print(res, end = "")
        wart = wart + 1
    res = ClientMultiSocket.recv(1024)
    res = res.decode('utf-8')
    print(res,end = "")
    while res != "OK\n":
        Input = input()
        ClientMultiSocket.send(str.encode(Input + "\n"))
        res = ClientMultiSocket.recv(1024)
        res = res.decode('utf-8')
        print(res,end = "")
    res = ClientMultiSocket.recv(1024)
    res = res.decode('utf-8')
    print(res,end = "")
    while res != "OK\n":
        Input = input()
        ClientMultiSocket.send(str.encode(Input + "\n"))
        res = ClientMultiSocket.recv(1024)
        res = res.decode('utf-8')
        print(res, end = "")
    taken_domin = domins2.index(Input.replace('CHOOSE ', ''))
    while wart != 3:
        res = ClientMultiSocket.recv(1024)
        res = res.decode('utf-8')
        print(res,end = "")
        res = ClientMultiSocket.recv(1024)
        res = res.decode('utf-8')
        print(res,end = "")
        wart = wart + 1
    fuj = fuj + 1

ClientMultiSocket.close()
